# This function creates a list of dictionaries with the
# raw table information from our form type.

from bs4 import BeautifulSoup
import requests


# iterate through each link of data
def get_sec_data(data_list):
    tables_data = []

    for data in data_list:
        table_link = data['filing']['cheat_link']
        # create a new dictionary each iteration to store the data
        table_data = {'headers': [], 'sections': [], 'data': []}

        content = requests.get(table_link).content
        data_soup = BeautifulSoup(content, features="html.parser")

        # find all the rows, figure out what type of row it is, parse the elements, and store the statement file list.
        for index, row in enumerate(data_soup.table.find_all('tr')):

            # first let's get all the elements.
            cols = row.find_all('td')

            # if it's a regular row and not a section or table header
            if len(row.find_all('th')) == 0 and len(row.find_all('strong')) == 0:

                reg_row = [ele.text.strip() for ele in cols]
                table_data['data'].append(reg_row)

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
