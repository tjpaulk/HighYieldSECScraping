from .db_connection import db_connection


def insert_filings_table(directory_list):
    cursor_object = db_connection()

    # Define the Insert Query.
    sql_insert = """
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
    """

    for filing in directory_list:
        value_list = []

        value = filing['filing']['report_num']

        cursor_object.execute("""SELECT report_num
                                FROM HighYieldSEC.dbo.filings_table 
                                WHERE report_num = '{}'""".format(value))

        exists = cursor_object.fetchone()

        print(exists)

        if exists is None:
            for x in filing['filing'].values():
                value_list.append(x)
            cursor_object.execute(sql_insert, value_list)
            cursor_object.commit()
            print('Row committed :', value_list)
        elif exists[0] == value:
            print('Filing already in database.')
        else:
            print('Houston, we have a problem!')
