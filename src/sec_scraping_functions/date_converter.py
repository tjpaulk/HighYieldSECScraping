import datetime as datetime

month_dict = {'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06',
              'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'}


def date_converter(date_str: str) -> datetime:

    x = date_str.replace('.', '').replace(',', '').replace(' ', '')

    new_date = x[-4:] + month_dict[x[:3].lower()] + x[(len(x)-6):-4]

    formatted_date = datetime.datetime.strptime(new_date, '%Y%m%d')

    return formatted_date


