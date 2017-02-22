##
# Class project 1 part 2: sqlite3
# Create db, create table, read in data
#
import sqlite3
import csv

def drop_table():
   with sqlite3.connect('greenhouse.db') as connection:
      curs = connection.cursor()
      curs.execute( 'DROP TABLE IF EXISTS greenhouse' )
   return True

def create_db():
   with sqlite3.connect('greenhouse.db') as connection:
      curs = connection.cursor()
      curs.execute("""CREATE TABLE greenhouse
         (time REAL, temp REAL)""")
      ## cursor.execute("""INSERT INTO greenhouse VALUES (79.0, )""")
   return True

def seed_data():
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
   create_db()
   seed_data()
