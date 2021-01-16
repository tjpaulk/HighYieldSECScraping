"""
    This function collects table sql_functions from a list of dictionaries

    :parameter  a list of dictionaries containing the interactive links created in function
    make_data_links

    creates a dictionary of table sql_functions from each link

    :returns a list of dictionaries for each tables sql_functions
"""
from bs4 import BeautifulSoup
import requests


# iterate through each link of sql_functions
def get_sec_data(data_list: list) -> list:
    tables_data = []

    for data in data_list:
        table_link = data['filing']['cheat_link']
        # create a new dictionary each iteration to store the sql_functions
        table_data = {'headers': [], 'sections': [], 'sql_functions': []}

        content = requests.get(table_link).content
        data_soup = BeautifulSoup(content, features="html.parser")

        # find all the rows, figure out what type of row it is, parse the elements, and store the statement file list.
        for index, row in enumerate(data_soup.table.find_all('tr')):

            # first let's get all the elements.
            cols = row.find_all('td')

            # if it's a regular row and not a section or table header
            if len(row.find_all('th')) == 0 and len(row.find_all('strong')) == 0:

                reg_row = [ele.text.strip() for ele in cols]
                table_data['sql_functions'].append(reg_row)

            # if it's a regular row and a section but not a table header
            elif len(row.find_all('th')) == 0 and len(row.find_all('strong')) != 0:

                sec_row = cols[0].text.strip()
                table_data['sections'].append(sec_row)

            # finally if it's not any of those it must be a header
            elif len(row.find_all('th')) != 0:

                hed_row = [ele.text.strip() for ele in row.find_all('th')]
                table_data['headers'].append(hed_row)

            else:
                print('We encountered an error.')

        # append it to the master list.
        tables_data.append(table_data)
    return tables_data
