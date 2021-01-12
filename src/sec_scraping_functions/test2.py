from bs4 import BeautifulSoup
import requests


# def some_func_name(link, cik, filing, ?)

content = requests.get("https://www.sec.gov/Archives/edgar/data//0001465885/000162828019002555/R3.htm").content
report_soup = BeautifulSoup(content, features="html.parser")

# The SEC html does not use unique identifiers for each row of data.  So far, the data I want
# has been at the top so if I create a list of table rows with the identifying data I am
# able to parse with, I can then index that list to zero.
# Instead of creating a separate named list for each item of data I want to collect for,
# I've created a generic list of lists so that it can be iterated over. rather than making multiple calls
mega_list = [[] for i in range(3)]  # index 0 = assets, index 1 = shares, index 2 = liabilities

soup_list = []


def parse_data_2(html_row, idx):
    test = [ele.text.strip() for ele in html_row.find_all('td')]
    parse_nums = [int(i) for i in test[idx].replace(',', '').split() if i.isdigit()]
    # print(test)
    # print(parse_nums[0])
    return parse_nums[0]  # indexing to 0 removes from list


for index, row in enumerate(report_soup.table.find_all('tr')[:]):
    soup_list.append(row)
    if 'defref_us-gaap_Assets' in str(row):
        mega_list[0].append(index)
    if 'defref_us-gaap_CommonStockSharesOutstanding' in str(row):
        mega_list[1].append(index)
    if 'defref_us-gaap_Liabilities' in str(row):
        mega_list[2].append(index)

test_dict = {'assets': parse_data_2(soup_list[mega_list[0][0]], 1),
             'liabilities': parse_data_2(soup_list[mega_list[2][0]], 1),
             'shares': parse_data_2(soup_list[mega_list[1][0]], 1),
             'new_shares': (parse_data_2(soup_list[mega_list[1][0]], 1) - parse_data_2(soup_list[mega_list[1][0]], 2)),
             'year_end': 'datetime',
             'cik_num': 'string',
             'div_paid': 'int',
             }
print(test_dict)

# return test_dict
