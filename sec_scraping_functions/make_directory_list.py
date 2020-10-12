# This function makes a list of dictionaries for all of the SEC reports for a company
# using it's CIK number.
from .make_url import make_url
from bs4 import BeautifulSoup
import requests


# base_url = r"https://www.sec.gov/Archives/edgar/data/"
# cik_num = '0001465885'


def make_directory_list(base_url, cik_num, limit=""):
    directory_list = []

    filing_directory = make_url(base_url, [cik_num, 'index.json'])

    data = requests.get(filing_directory).json()
    if limit == "":
        limit = (len(data['directory']['item']) - 1)

    for item in data['directory']['item'][:limit]:

        collection_dict = {}

        # cleaning up empty data field
        item.pop('size')

        add_dash = item['name'][:-6] + '-' + item['name'][-6:]
        second_dash = add_dash[:-9] + '-' + add_dash[-9:] + '-index.html'
        report_url = make_url(
            base_url, [cik_num, item['name'] + '/' + second_dash])

        collection_dict['filing'] = {}
        collection_dict['filing']['report_num'] = item['name']
        collection_dict['filing']['filing_date'] = item['last-modified'][:10]
        collection_dict['filing']['url'] = report_url
        # collect and add form type
        content = requests.get(report_url).content
        report_soup = BeautifulSoup(content, features='html.parser')
        # using 'strong' is a pretty weak way to grab the form type.
        # plus I also want the description
        form_type = report_soup.find('strong').text
        collection_dict['filing']['report_type'] = form_type
        collection_dict['filing']['cik_num'] = cik_num

        directory_list.append(collection_dict)

    return directory_list
