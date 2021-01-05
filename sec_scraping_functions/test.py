from datetime import datetime
from bs4 import BeautifulSoup, element, NavigableString
import requests
import bs4


# Make the dictionary a dictionary of key year / month to contain the dictionaries field / data
def test(cik_num, link_list):
    dummy_dict = {'cik_num': cik_num,
                  'filing_date': 'filing date',
                  'defref_us-gaap_CashAndCashEquivalentsAtCarryingValue': float('NaN'),
                  'defref_us-gaap_Assets': float('NaN'),
                  'defref_us-gaap_CommonStockValue': float('NaN'),
                  'test': float('Nan')}

    for link in link_list:
        content = requests.get(link[1]).content
        report_soup = BeautifulSoup(content, features="html.parser")

        for index, row in enumerate(report_soup.table.find_all('tr')[:]):

            if index == 0:
                reg_row = [ele.text.strip() for ele in row.find_all('th')]
                dummy_dict['filing_date'] = strip_punc = reg_row[1].replace(',', "").replace('.', '')
                # print(strip_punc)
                # dt = datetime.strptime(strip_punc, '%b %d %Y')
                # print(dt, type(dt))

            for key, value in dummy_dict.items():
                # Must convert bs4 object to string to be able to search for identifying text string
                # in bs4 objects.  By using SEC JS / CSS onclick parameter, the desired data can be
                # isolated to extract without have to collect all row data.
                if key in str(row):

                    if key == 'defref_us-gaap_CommonStockValue':
                        # takes the number of common shares from the text field since it is more complete than the
                        # number field.
                        reg_row = [ele.text.strip() for ele in row.find_all('td')]
                        parce_nums = [int(i) for i in reg_row[0].replace(',', '').split() if i.isdigit()]
                        dummy_dict[key] = parce_nums[2]
                    elif len(row.find_all('td')) != 0 and row.find_all(class_="nump"):
                        reg_row = [ele.text.strip() for ele in row.find_all('td')]

                        dummy_dict[key] = [int(i) for i in reg_row[1].replace(',', '').replace('u', ' ').split() if i.isdigit()][0]

                        print('Success')
        print('The result is :', dummy_dict)
