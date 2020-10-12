import unittest
import sys
sys.path.append('E:/MyPyProjects/SECWebScraping/sec_scraping_functions')
from sec_scraping_functions import *


class MyTestCase(unittest.TestCase):
    def test_make_url(self):
        base = 'www.does'
        components = ['this', 'work?']
        result = make_url(base, components)
        self.assertEqual('www.does/this/work?', result)

    def test_make_directory_list(self):
        expected = {'filing': {'cik_num': '0001465885', 'report_num': '000117911020009701', 'filing_date': '2020-09-11',
                               'url': 'https://www.sec.gov/Archives/edgar/data//0001465885/'
                                      '000117911020009701/0001179110-20-009701-index.html', 'report_type': 'Form 4'}}
        base_url = r"https://www.sec.gov/Archives/edgar/data/"
        cik_num = '0001465885'
        result = make_directory_list(base_url, cik_num, 1)
        # to test against full list remove 3rd parameter
        self.assertEqual(expected, result[0])

    def test_select_form_list(self):
        expected = {'filing': {'cik_num': '0001465885', 'report_num': '000162828020003097', 'filing_date': '2020-03-05',
                               'url': 'https://www.sec.gov/Archives/edgar/data//0001465885/'
                                      '000162828020003097/0001628280-20-003097-index.html', 'report_type': 'Form 10-K'}}
        base_url = r"https://www.sec.gov/Archives/edgar/data/"
        cik_num = '0001465885'
        directory = make_directory_list(base_url, cik_num, 50)
        form_type = 'Form 10-K'
        result = select_form_list(directory, form_type)
        self.assertEqual(expected, result[0])

    def test_make_data_links(self):
        expected = [["https://www.sec.gov/cgi-bin/viewer?action=view&cik="
                     "0001465885&accession_number=0001628280-20-003097&xbrl_type=v#",
                     "https://www.sec.gov/Archives/edgar/data//0001465885/000162828020003097/R2.htm"]]
        cik_num = '0001465885'
        form_type_list = [{'filing': {'report_num': '000162828020003097', 'filing_date': '2020-03-05',
                                      'url': 'https://www.sec.gov/Archives/edgar/data//0001465885/000162828020003097/'
                                             '0001628280-20-003097-index.html', 'report_type': 'Form 10-K'}}]
        links = make_data_links(form_type_list, cik_num)
        self.assertEqual(expected, links)

    def test_get_sec_data(self):
        with open('UnitTestsData/test_get_sec_data.csv', 'r') as f:
            expected = f.read()
        list(expected)
        list_dict = [{'filing': {'cik_num': '0001465885',
                                 'report_num': '000162828020003097', 'filing_date': '2020-03-05',
                                 'url': 'https://www.sec.gov/Archives/edgar/data//0001465885/000162828020003097/'
                                        '0001628280-20-003097-index.html', 'report_type': 'Form 10-K',
                                 'interactive_url': 'https://www.sec.gov/cgi-bin/viewer?action=view&cik='
                                                    '0001465885&accession_number=0001628280-20-003097&xbrl_type=v#',
                                 'cheat_link': 'https://www.sec.gov/Archives/edgar/data//0001465885/'
                                               '000162828020003097/R2.htm'}}]
        result = get_sec_data(list_dict)
        # had to convert the function data to a string to compare to expected data.
        result1 = str(result)
        self.assertEqual(expected, result1)


if __name__ == '__main__':
    unittest.main()
