# takes a directory of forms and picks out all of the forms of a
# desired type and creates a list of dictionaries.


def select_form_list(directory, form_type, limit=""):
    form_type_list = []

    if limit == "":
        limit = (len(directory) - 1)

    for form in directory[:limit]:
        if form['filing']['report_type'] == form_type:
            form_type_list.append(form)

    return form_type_list
