from src.sec_scraping_functions import make_directory_list
from src.sql_functions import table_templates
from src.csv_json_xml_functions.save_to_csv import *

import csv
from os import path
import os

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


cik_list: list = [{'GGN': '0001313510'}, {'SUNS': '0001508171'}, {'GOF': '0001380936'},
                  {'GAIN': '0001321741'}, {'FDUS': '0001513363'}, {'WMC': '0001465885'}]
table_name: str = 'filings_table'
test = []


for cik_dict in cik_list[:1]:
    for key, cik_num in cik_dict.items():

        directory_list = make_directory_list(
            "https://www.sec.gov/Archives/edgar/data/", cik_num)

        table_name = 'filings_table'
        table = table_templates(table_name)

        # insert_filings_table(directory_list, table, table_name)

        save_to_csv(directory_list)



        # toCSV = directory_list
        # keys = toCSV[0].keys()
        # csv_file = '../sec_data_files/test.csv'
        # csv_file_exists = os.path.isfile(csv_file)
        #
        # with open(csv_file, 'a', newline='') as output_file:
        #     dict_writer = csv.DictWriter(output_file, keys)
        #     if not csv_file_exists:
        #         dict_writer.writeheader()
        #         dict_writer.writerows(toCSV)
        #         print('CSV file created.')
        #     else:
        #         with open(csv_file, 'r') as read_file:
        #             report_nums = []
        #             for line in read_file.readlines():
        #                 array = line.split(',')
        #                 report_num = array[0]
        #                 report_nums.append(report_num)
        #
        #             for row in toCSV:
        #                 exists = False
        #                 for num in report_nums:
        #                     exists = (row['report_num'] == num)
        #                     if exists:
        #                         print('filing is already listed.')
        #                         break
        #
        #                 if not exists:
        #                     dict_writer.writerow(row)
        #                     print('New line of data added.')
