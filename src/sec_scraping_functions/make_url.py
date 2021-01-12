"""
    Takes a root URL and a list of components

    :parameter (string of base url, list of string components)

    :returns a string containing a url
"""


def make_url(base_url: str, components: list) -> str:

    complete_url = base_url

    for comp in components:
        complete_url = '{}/{}'.format(complete_url, comp)

    return complete_url
