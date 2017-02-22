##
#  Class project 1 part 2: sqlite3
#  Create db, create table, read in data
#
import sqlite3
NameEmailDbName = '../db/NameEmail.db'

##
#  If the table exists, drop it
#  Makes it easy to start fresh
#
def drop_table():
   with sqlite3.connect( NameEmailDbName ) as connection:
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
   with sqlite3.connect( NameEmailDbName ) as connection:
      curs = connection.cursor()
      curs.execute(
         """CREATE TABLE NameEmail
            ( name TEXT,
              email TEXT,
              site TEXT,
              active INTEGER,
              date_added INTEGER,
              date_changed INTEGER )""")
   return True

##
#  Seed the table
#  Insert a row (or two) in the table, as a sanity check
#
def seed_table():
   with sqlite3.connect( NameEmailDbName ) as connection:
      curs = connection.cursor()
      curs.execute(
         """INSERT INTO NameEmail VALUES
            ( 'Joe', 'joe@joe.com', 'groja.com', 1, 1487799078, 1487799078 )""")
   return True

##
# For possible future reference
#
import csv
def foobar_unused():
   # open db, open datafile, iterate through datafile, running INSERT
   with sqlite3.connect('greenhouse.db') as connection:
      curs = connection.cursor()
      with open( 'DataTemp1.dat' ) as data:
         reader = csv.reader( data )
         for row in reader:
            print( 'Inserting row:', row )   # to see the data
            curs.execute( "INSERT INTO greenhouse VALUES (?, ?)", row )

if __name__ == '__main__':
   drop_table()
   create_table()
   seed_table()
