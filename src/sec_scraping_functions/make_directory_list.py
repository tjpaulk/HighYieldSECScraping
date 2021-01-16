from typing import Dict, List, Any

from .make_url import make_url
from bs4 import BeautifulSoup
from src.sql_functions import get_most_recent_filing
import requests


def make_directory_list(base_url: str, cik_num: str, limit: int = "") -> list:
    """
    This function creates a list of dictionaries containing all filings for a company based on its
    cik number.  The list is then stored in the database elsewhere in the project.

    Parameters
    ----------
    base_url : str
        A string containing the root url.
    cik_num : str
        A string with the company cik number being researched.
    limit : int, optional
        An optional parameter used to limit the number of filings returned.  Primarily used to speed up unit testing.

    Returns
    -------
        A list of dictionaries containing information about each filing found.
    """

    directory_list = []

    filing_directory = make_url(base_url, [cik_num, 'index.json'])

    # Get's the latest filing saved in db.
    last_saved = get_most_recent_filing(cik_num)
    if not last_saved:  # If there are no filings assign a default value to last_saved.
        last_saved = 'empty'

    data = requests.get(filing_directory).json()

    if limit == "":
        limit = (len(data['directory']['item']) - 1)

    for item in data['directory']['item'][:limit]:

        if (last_saved[0] == item['name']) and (last_saved[0] != '000117911020009701'):
            # Checks if the current filing exists in the db and returns the 'directory_list' if true.
            # Skips the unit test filing.
            return directory_list
        else:

            # cleaning up empty sql_functions field
            item.pop('size')

            # Modify item['name'] to create a working report url.
            add_dash = item['name'][:-6] + '-' + item['name'][-6:]
            second_dash = add_dash[:-9] + '-' + add_dash[-9:] + '-index.html'
            report_url = make_url(
                base_url, [cik_num, item['name'] + '/' + second_dash])

            content = requests.get(report_url).content
            report_soup = BeautifulSoup(content, features='html.parser')
            form_type = report_soup.find('strong').text
            form_name = report_soup.find(id="formName").get_text()

            # removing 'filing' level key - likely not needed if creating a list
            collection_dict = {'report_num': item['name'],
                               'filing_date': item['last-modified'][:10],
                               'url': report_url,
                               'report_type': form_type,
                               'report_name': form_name[1:-8],
                               'cik_num': cik_num}

            directory_list.append(collection_dict)

    return directory_list
