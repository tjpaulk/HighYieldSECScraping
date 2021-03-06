from src.sql_functions import db_connection


def get_filings_by_type(cik_num: str, form_type: str) -> list:
    """
    Selects all filings of a specific form type for a given cik number from the database.
    Returns a list lists containing the filing date and filing link.

    Parameters
    ----------
    cik_num : str
        A string containing the cik number.
    form_type : str
        A string containing the desired form type.

    Returns
    -------
        A list of list pairs containing the filing date and filing link.
    """

    filing_by_type = \
        """
        SELECT TOP (10) [filing_date],[url],[report_num]
        FROM [HighYieldSEC].[dbo].[filings_table]
        WHERE [report_type] = '{}' AND [cik_num] = '{}'
        ORDER BY [filing_date] DESC
        """.format(form_type, cik_num)

    cursor_object = db_connection()
    cursor_object.execute(filing_by_type)
    type_list = cursor_object.fetchall()

    assert isinstance(type_list, object)
    return type_list
