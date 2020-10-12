

# this function takes a root URL and combines a list of components to return a complete URL
def make_url(base_url, components):

    complete_url = base_url

    for c in components:
        complete_url = '{}/{}'.format(complete_url, c)

    return complete_url
