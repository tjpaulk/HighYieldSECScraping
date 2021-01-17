from bs4 import BeautifulSoup
from datetime import date
import requests


# should work for 1 company- cik 0001465885.  Need to research further as other companies may list
# data differently on sec interactive tables.
def make_data_list(links: str, cik: str) -> list:
    share_data: list = []
    for pair in links:
        link = pair[1]

        content = requests.get(link).content
        report_soup = BeautifulSoup(content, features="html.parser")

        # The SEC html does not use unique identifiers for each row of sql_functions.  So far, the sql_functions I want
        # has been at the top so if I create a list of table rows with the identifying sql_functions I am
        # able to parse with, I can then index that list to zero.
        # Instead of creating a separate named list for each item of sql_functions I want to collect for,
        # I've created a generic list of lists so that it can be iterated over. rather than making multiple calls
        mega_list = [[] for i in range(4)]  # index 0 = assets, index 1 = shares, index 2 = liabilities
        soup_list = []
        filing_date: date = None
        assets = None
        liabilities = None
        shares = None
        div_paid = None

        def parse_data_2(html_row, idx):
            test = [ele.text.strip() for ele in html_row.find_all('td')]
            parse_nums = [int(i) for i in test[idx].replace(',', '').split() if i.isdigit()]
            if parse_nums:
                return parse_nums[0]
            else:
                return 0

        for index, row in enumerate(report_soup.table.find_all('tr')[:]):
            soup_list.append(row)

            if 'defref_us-gaap_Assets' in str(row):
                mega_list[0].append(index)
                if mega_list[0]:
                    assets = parse_data_2(soup_list[mega_list[0][0]], 1)
                else:
                    assets = None
            elif 'defref_us-gaap_CommonStockSharesOutstanding' in str(row):
                mega_list[1].append(index)
                if mega_list[1]:
                    shares = parse_data_2(soup_list[mega_list[1][0]], 1)
                else:
                    shares = None
            elif 'defref_us-gaap_Liabilities' in str(row):
                mega_list[2].append(index)
                if mega_list[2]:
                    liabilities = parse_data_2(soup_list[mega_list[2][0]], 1)
                else:
                    liabilities = None
            elif index == 0 and 'Consolidated Balance Sheets' in str(row):
                for i, line in enumerate(row.find_all('th')):
                    if i == 1:
                        filing_date = line.text.strip()
            else:
                continue

        temp_dict = {'filing_number': link[-25:-7],
                     'assets': assets,
                     'liabilities': liabilities,
                     'shares': shares,
                     'new_shares': (parse_data_2(soup_list[mega_list[1][0]], 1) - parse_data_2(soup_list[mega_list[1][0]], 2)),
                     'year_end': filing_date,
                     'cik_num': cik,
                     'div_paid': div_paid
                     }

        share_data.append(temp_dict)

    return share_data
