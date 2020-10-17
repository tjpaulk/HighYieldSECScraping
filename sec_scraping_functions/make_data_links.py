"""
    Takes a list dictionaries with links to the desired form type and string of the cik
    number

    :returns a list of url links to the specific SEC interactive table

    Future changes in mind
    1) add parameter to take the table reference- ie R2.htm for more versatility
    2) consider changing to create teh url link as needed instead of a list or both
"""


def make_data_links(form_list: list, cik_num: str, table_ref: str) -> list:
    links = []
    for form in form_list:
        link = form['filing']['url']
        accession = link[-31:-11]

        form['filing'][
            'interactive_url'] = "https://www.sec.gov/cgi-bin/viewer?action=view&cik=" \
                                 "{}&accession_number={}&xbrl_type=v#".format(
            cik_num, accession)
        form['filing']['cheat_link'] = r"https://www.sec.gov/Archives/edgar/data//0001465885/" + \
                                       form['filing']['report_num'] + table_ref  # "/R2.htm"
        links.append([form['filing']['interactive_url'], form['filing']['cheat_link']])

    return links
