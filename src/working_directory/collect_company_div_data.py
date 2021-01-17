from make_data_list import make_data_list
from sec_scraping_functions import make_data_links
from sql_functions import get_filings_by_type

cik_list: list = [{'GGN': '0001313510'}, {'SUNS': '0001508171'}, {'GOF': '0001380936'},
                  {'GAIN': '0001321741'}, {'FDUS': '0001513363'}, {'WMC': '0001465885'}]
table_name: str = 'filings_table'
form_type: list = ["Form 10-K"]
table_ref: str = 'R3.htm'

# for cik_dict in cik_list[:3]:
#     for cik_num in cik_dict.values():
#         print(cik_num)
keys = list(cik_list[5].keys())
cik_num = list(cik_list[5].values())
# print(cik_num)

filings_list = get_filings_by_type(cik_num[0], form_type[0])
# for item in filings_list:
#     print(item)

data_links = make_data_links(filings_list, cik_num[0], table_ref)
# for item in data_links:
#     print(item)

sec_data = make_data_list(data_links, cik_num[0])
print(sec_data)

