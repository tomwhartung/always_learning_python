##
#  Database utility functions
#
import sqlite3

##
#  Function to drop the bitcoin table
#
def drop_table():
    with sqlite3.connect('bitcoin.db') as connection:
        c = connection.cursor()
        c.execute("""DROP TABLE IF EXISTS currency;""")
    return True

##
#  Function to create the bitcoin database
#
def create_db():
    with sqlite3.connect('bitcoin.db') as connection:
        c = connection.cursor()
        c.execute("""CREATE TABLE currency (
                     exchange text,
                     price REAL,
                     horah DATETIME DEFAULT CURRENT_TIMESTAMP
                 );""")
    return True

##
#  Run the app: drop and (re)create the database
#
if __name__ == '__main__':
    print( 'Dropping the table' )
    drop_table()
    print( 'Creating the database' )
    create_db()
