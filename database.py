import sqlite3

#Connect to the database
#if the database doesnot exixt, SQlite creaets it.

def get_connection():
    connection = sqlite3.connect("ExpenseTracker.db")
    connection.row_factory = sqlite3.Row
    return connection

#Create the expense table.
def create_table():
    connection= get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()
#Run this function when the application starts
create_table()

#Working Mechanism

#sqlite3.connect()  connects to the database.
#CREATE TABLE creates a table if it doesnt alreadt exist.
#id gives every expense a unique number.
# item stores what you purchased.
# category stores the expense category.
# date stores the transaction date.