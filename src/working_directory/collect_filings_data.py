from src.sec_scraping_functions import make_directory_list
from src.sql_functions import table_templates
from src.sql_functions import insert_filings_table
from src.csv_json_xml_functions.save_to_csv import *
from src.csv_json_xml_functions.save_to_json import *
from src.csv_json_xml_functions.save_to_xml import *



"""
    This module is for proof of concept of the goal to scrape SEC information and store specific 
    desired parts of that information into SQL, CSV, JSON and XML sql_functions structures.
    
    It will take a random list of high dividend stock cik numbers and save the following information:
        * filing report number
        * filing date 
        * url link to the report 
        * cik number
        * filing report name
        
    This information be store for use by the next proof of concept module collect_company_div_data.
"""


csv_file = '../sec_data_files/filing_list.csv'
json_file = '../sec_data_files/filing_list.json'
cik_list: list = [{'GGN': '0001313510'}, {'SUNS': '0001508171'}, {'GOF': '0001380936'},
                  {'GAIN': '0001321741'}, {'FDUS': '0001513363'}, {'WMC': '0001465885'}]
table_name: str = 'filings_table'
test = []


for cik_dict in cik_list[:3]:
    for cik_num in cik_dict.values():

        directory_list = make_directory_list(
            "https://www.sec.gov/Archives/edgar/data/", cik_num)
        if not directory_list:
            continue

        table_name = 'filings_table'
        table = table_templates(table_name)

        # insert_filings_table(directory_list, table, table_name)

        # save_to_csv(directory_list, csv_file)

        # save_to_json(directory_list, json_file)

        # not yet implemented
        # save_to_xml(directory_list)
