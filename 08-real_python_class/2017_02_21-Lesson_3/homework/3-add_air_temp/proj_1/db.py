##
# Class project 1 part 2: sqlite3
# Create db, create table, read in data
#
import sqlite3
import csv
DATA_TEMP_1 = '../data/DataTemp1.dat'
DATA_TEMP_3 = '../data/DataTemp3.dat'
GREENHOUSE_DB = '../db/greenhouse.db'

def drop_table():
   with sqlite3.connect( GREENHOUSE_DB ) as connection:
      curs = connection.cursor()
      curs.execute( 'DROP TABLE IF EXISTS greenhouse' )
   return True

def create_db():
   with sqlite3.connect( GREENHOUSE_DB ) as connection:
      curs = connection.cursor()
      schema = 'CREATE TABLE greenhouse (time REAL, temp_1 REAL, temp_3 REAL)'
      curs.execute( schema )
   return True

def seed_data():
   # open db, open datafile, iterate through datafile, running INSERT
   with sqlite3.connect( GREENHOUSE_DB ) as connection:
      curs = connection.cursor()
      with open( DATA_TEMP_1 ) as data:
         reader = csv.reader( data )
         for row in reader:
            print( 'Inserting row:', row )   # to see the data
            curs.execute( "INSERT INTO greenhouse(time,temp_1) VALUES (?, ?)", row )
      with open( DATA_TEMP_3 ) as data:
         reader = csv.reader( data )
         for row in reader:
            print( 'Inserting row:', row )   # to see the data
            curs.execute( "INSERT INTO greenhouse(time,temp_3) VALUES (?, ?)", row )

if __name__ == '__main__':
   drop_table()
   create_db()
   seed_data()
