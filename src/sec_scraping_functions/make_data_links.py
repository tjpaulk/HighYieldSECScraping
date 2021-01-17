"""
    Takes a list dictionaries with links to the desired form type and string of the cik
    number

    :returns a list of url links to the specific SEC interactive table

    Future changes in mind
    1) add parameter to take the table reference- ie R2.htm for more versatility
    2) consider changing to create teh url link as needed instead of a list or both
"""


def make_data_links(form_list: list, cik_num: str, table_ref: str) -> list:
    links: list = []
    for form in form_list:
        # link = form['filing']['url']
        link = form[1]
        accession_tuple: tuple = link[-31:-11]

        accession_str: str = ''.join(accession_tuple)

        link1: str = r"https://www.sec.gov/cgi-bin/viewer?action=view&cik={}&accession_number={}&xbrl_type=v#"\
                     .format(cik_num[0], accession_str),
        # form['filing']['cheat_link'] = \
        link2: str = r"https://www.sec.gov/Archives/edgar/data//0001465885/{}/{}".format(form[2], table_ref)

        link_list: list = [link1[0], link2]

        links.append(link_list)

    return links
