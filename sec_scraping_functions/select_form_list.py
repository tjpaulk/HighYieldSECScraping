"""
    Picks out desired forms of a single type.
    :parameter (list of dictionary containing filings, string of the form desired,
                optional integer limiter to restrict the number of forms returned)

    :returns at list of the forms requested.
"""


def select_form_list(directory: list, form_type: str, limit="") -> list:
    form_type_list = []

    if limit == "":
        limit = (len(directory) - 1)

    for form in directory[:limit]:
        if form['filing']['report_type'] == form_type:
            form_type_list.append(form)

    return form_type_list
