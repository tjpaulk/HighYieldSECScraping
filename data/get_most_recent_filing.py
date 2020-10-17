from data import db_connection


def get_most_recent_filing(cik_num: str) -> str:

    check_filing = \
        """
        SELECT TOP (1) [report_num]
        FROM [HighYieldSEC].[dbo].[filings_table]
        WHERE [cik_num] = '{}'
        ORDER BY [filing_date] DESC
        """.format(cik_num)

    cursor_object = db_connection()
    cursor_object.execute(check_filing)
    latest = cursor_object.fetchone()
    print(latest)
    return latest
