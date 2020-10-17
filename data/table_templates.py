"""
    Function takes a key as parameter and returns a string value of a table insertion template.

    :parameter (str dictionary key)

    :returns string template for db table insertion
"""


def table_templates(key: str) -> str:
    template_dict = \
        {
            'filings_table':
            """
            INSERT INTO [HighYieldSEC].[dbo].[filings_table]
             (
                [report_num],
                [filing_date],
                [url],
                [report_type],
                [cik_num]
            )
            VALUES
            (
                ?, ?, ?, ?, ?
            )
            """,
            'sec_data':
            """
            INSERT INTO [HighYieldSEC].[dbo].[sec_data]
             (
                [date_filed],
                [cik_num],
                [total_assets],
                [total_liabilities],
                [common_shares],
                [div_paid]
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?
            )
            """
        }

    return template_dict[key]
