from make_data_list import make_data_list
from save_to_csv import save_to_csv
from save_to_json import save_to_json
from sec_scraping_functions import make_data_links
from sql_functions import get_filings_by_type, insert_filings_table, table_templates

cik_list: list = [{'GGN': '0001313510'}, {'SUNS': '0001508171'}, {'GOF': '0001380936'},
                  {'GAIN': '0001321741'}, {'FDUS': '0001513363'}, {'WMC': '0001465885'}]

form_type: list = ["Form 10-K"]
table_ref: str = 'R3.htm'
json_file = '../sec_data_files/stock_data.json'
csv_file = '../sec_data_files/stock_data.csv'

table_name: list =['filings_table', 'sec_data']
# table = table_templates(table_name[index])

keys = list(cik_list[5].keys())
cik_num = list(cik_list[5].values())

filings_list = get_filings_by_type(cik_num[0], form_type[0])

data_links = make_data_links(filings_list, cik_num[0], table_ref)

sec_data = make_data_list(data_links, cik_num[0])

# save_to_json(sec_data, json_file)
#
# save_to_csv(sec_data, csv_file)

# insert_filings_table(sec_data, table, table_name)
