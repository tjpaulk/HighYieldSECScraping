from .db_connection import db_connection


# def insert_filings_table(directory_list: list) -> None:
def insert_filings_table(insert_list: list, table: str, table_name: str) -> None:
    """
    Currently for table filings_table, checks to see if a filing is already stored in db and
    adds only if it is not.  I hope to enable this function to do bulk inserts into multiple db tables.

    Parameters
    ----------
    insert_list : list
        A list containing filing directories.
    table : str
        A string document currently containing formatting to insert into the filings_table of the db.
    table_name : str
        A string of the table name.

    Returns
    -------
    None

    Future:  Look at inserting all of the sql_functions at once instead of looping through.  Perhaps
    by using a dataframe or list of lists.

    Eventually save only certain form types since most will never be used.  Need to figure out
    which ones to keep for differing company types.
    """

    cursor_object = db_connection()

    for filing in insert_list:
        value_list = []

        value = filing['report_num']
        print('value : ', value)
        cursor_object.execute("""SELECT report_num
                                FROM HighYieldSEC.dbo.{} 
                                WHERE report_num = '{}'""".format(table_name, value))

        exists = cursor_object.fetchone()

        if exists is None:
            for x in filing.values():
                value_list.append(x)

            cursor_object.execute(table, value_list)
            cursor_object.commit()
        elif exists[0] == value:
            # print('Filing already in database.')
            pass
        else:
            print('Houston, we have a problem!')
