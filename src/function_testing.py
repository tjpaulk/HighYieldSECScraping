from src.sec_scraping_functions import make_directory_list
from src.sql_functions import table_templates
from src.sql_functions import get_filings_by_type
from src.sec_scraping_functions import make_data_links, test
"""
    This exists as it is because the project got messed up when I switched to VS Code because
    pyCharm Community edition does not support db.  Turned out to be unnecessary but still have
    some issues regarding pathing.

    This module is where I started interacting with the db within the project.
"""

# import sys
# sys.path.append('../sec_scraping_functions')


directory_list = make_directory_list(
    "https://www.sec.gov/Archives/edgar/data/", '0001380936')

table_name = 'filings_table'
table = table_templates(table_name)

# insert_filings_table(directory_list, table, table_name)

filings_list = get_filings_by_type('0001465885', "Form 10-K")
data_links = make_data_links(filings_list, '0001465885', '/R2.htm')
test('0001465885', data_links)
