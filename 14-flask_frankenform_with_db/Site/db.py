##
#  Class project 1 part 2: sqlite3
#  Create db, create table, read in data
#
import sqlite3
DB_DIRECTORY = '../db/'
NAME_EMAIL_TABLE = DB_DIRECTORY + 'NameEmail.db'

##
#  If the table exists, drop it
#  Makes it easy to start fresh
#
def drop_table():
   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
      curs = connection.cursor()
      curs.execute( 'DROP TABLE IF EXISTS NameEmail' )
   return True

##
#  Create the table
#  If the database doesn't exist, this will create it as well
#  Reference: https://www.sqlite.org/datatype3.html
#  Note: date_* columns are stored as integers:
#     "INTEGER as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC"
#
def create_table():
   ## with sqlite3.connect( '../db/NameEmail.db' ) as connection:
   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
      curs = connection.cursor()
      curs.execute(
         """CREATE TABLE NameEmail
            ( name TEXT,
              email TEXT,
              site TEXT,
              active INTEGER,
              date_added INTEGER,
              date_changed INTEGER,
              consulting INTEGER DEFAULT 0,
              newsletter INTEGER DEFAULT 0,
              portrait INTEGER DEFAULT 0
            )""")
   return True

##
#  Seed the table
#  Insert a row (or two) in the table, as a sanity check
#
def seed_table():
   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
      curs = connection.cursor()
      curs.execute(
         """INSERT INTO NameEmail VALUES
            ( 'Joe', 'joe@joe.com', 'groja.com', 1, 1487799078, 1487799078, 0, 0, 0 )
         """)
   return True

##
#  Print all rows in the table to stdout
#
def print_table():
   rows = get_data()
   see_data( rows )
   return True

##
#  Get the data
#
def get_data():
   rows = []
   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
      curs = connection.cursor()
      curs.execute( 'SELECT * from NameEmail')
      rows = curs.fetchall()
      ## print( 'Calling see_data 1' )
      ## see_data( rows )
   return rows

##
#  Print the data
#
def see_data( rows ):
   for row in rows:
      print( "row:", row )
   return True

##
# Mainline code to drop, create, seed and print the table
#
if __name__ == '__main__':
   drop_table()
   create_table()
   seed_table()
   print_table()
