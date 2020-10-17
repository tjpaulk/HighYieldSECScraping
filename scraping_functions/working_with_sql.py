"""
    This exists as it is because the project got messed up when I switched to VS Code because
    pyCharm Community edition does not support db.  Turned out to be unnecessary but still have
    some issues regarding pathing.

    This module is where I started interacting with the db within the project.
"""

import sys
# sys.path.append('E:/MyPyProjects/SECWebScraping/data')
sys.path.append('../sec_scraping_functions')
from sec_scraping_functions import make_directory_list
from data import insert_filings_table, table_templates


directory_list = make_directory_list(
    "https://www.sec.gov/Archives/edgar/data/", '0001465885', 5)

table_name = 'filings_table'
table = table_templates(table_name)

# insert_filings_table(directory_list)
insert_filings_table(directory_list, table, table_name)

