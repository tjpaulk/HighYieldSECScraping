import sys
# sys.path.append('E:/MyPyProjects/SECWebScraping/data')
sys.path.append('../sec_scraping_functions')
from sec_scraping_functions import make_directory_list
from data import insert_filings_table


directory_list = make_directory_list(
    "https://www.sec.gov/Archives/edgar/data/", '0001313510')
# print(directory_list)

insert_filings_table(directory_list)
