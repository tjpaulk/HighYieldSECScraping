# Create links to interactive data on Edgar website


def make_data_links(form_list, cik_num):
    links = []
    for form in form_list:
        link = form['filing']['url']
        accession = link[-31:-11]

        form['filing'][
            'interactive_url'] = "https://www.sec.gov/cgi-bin/viewer?action=view&cik={}&accession_number={}&xbrl_type=v#".format(
            cik_num, accession)
        form['filing']['cheat_link'] = r"https://www.sec.gov/Archives/edgar/data//0001465885/" + form['filing'][
            'report_num'] + "/R2.htm"
        links.append([form['filing']['interactive_url'], form['filing']['cheat_link']])

    return links
