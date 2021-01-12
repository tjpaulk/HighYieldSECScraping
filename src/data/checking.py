# To be deleted.  This was taken from the template this section of the project was
# created from and only exists as reference material.

import pyodbc

create_sec_data = """
-- Create the table if it does not exist.
IF Object_ID('sec_data') IS NULL

CREATE TABLE [HighYieldSEC].[dbo].[sec_data]
(
    [date_filed] DATETIME NOT NULL,
    [cik_num] NVARCHAR(10) NOT NULL,
    [total_assets] INT NULL,
    [total_liabilities] INT NULL,
    [common_shares] INT NULL,
    [div_paid] INT NULL,
)
"""

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

cursor_object.execute(create_sec_data)

cursor_object.commit()
