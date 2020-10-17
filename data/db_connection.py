"""
    Creates a database connection using pyodbc.  May switch to sqlAlchemy at some point when I
    become more familiar with working with db's.
    :parameter (none)

    :returns a cursor object to be used elsewhere.

    Future goal:  Can this be done using a with command?
"""

import pyodbc


def db_connection() -> object:
    # Connection string
    DRIVER = '{ODBC Driver 17 for SQL Server}'
    SERVER_NAME = "localhost\\SQLEXPRESS"
    DATABASE_NAME = "HighYieldSEC"

    CONNECTION_STRING = r"""
    Driver={driver};
    Server={server};
    Database={database};
    Trusted_Connection=yes;
    """.format(
        driver=DRIVER,
        server=SERVER_NAME,
        database=DATABASE_NAME
    )

    connection_object: pyodbc.Connection = pyodbc.connect(CONNECTION_STRING)

    cursor_object: pyodbc.Cursor = connection_object.cursor()
    return cursor_object
