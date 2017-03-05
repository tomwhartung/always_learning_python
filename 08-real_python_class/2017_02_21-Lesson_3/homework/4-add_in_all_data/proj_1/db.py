##
# Class project 1 part 2: sqlite3
# Create db, create table, read in data
#
import sqlite3
import csv
## DATA_TEMP_1 = '../data/DataTemp1.dat'
## DATA_TEMP_3 = '../data/DataTemp3.dat'
DATA_FILE_BASE = '../data/DataTemp'
DATA_FILE_NUMBERS = ["1", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
DATA_FILE_EXTENSION = '.dat'
GREENHOUSE_DB = '../db/greenhouse.db'

##
#  Our schema always changes and we are always needing to drop this db
#
def drop_table():
   with sqlite3.connect( GREENHOUSE_DB ) as connection:
      curs = connection.cursor()
      curs.execute( 'DROP TABLE IF EXISTS greenhouse' )
   return True

##
#  This function creates the db and contains our schema
#
def create_db():
   with sqlite3.connect( GREENHOUSE_DB ) as connection:
      curs = connection.cursor()
      schema = 'CREATE TABLE greenhouse ( '
      schema += 'unix_time REAL'
      schema += ', temp_1 REAL DEFAULT 0'
      schema += ', temp_3 REAL DEFAULT 0'
      schema += ', temp_4 REAL DEFAULT 0'
      schema += ', temp_5 REAL DEFAULT 0'
      schema += ', temp_6 REAL DEFAULT 0'
      schema += ', temp_7 REAL DEFAULT 0'
      schema += ', temp_8 REAL DEFAULT 0'
      schema += ', temp_9 REAL DEFAULT 0'
      schema += ', temp_10 REAL DEFAULT 0'
      schema += ', temp_11 REAL DEFAULT 0'
      schema += ', temp_12 REAL DEFAULT 0'
      schema += ', temp_13 REAL DEFAULT 0)'
      curs.execute( schema )
   return True

##
#  Open db, get data from datafile, iterate through data running INSERT
#
def seed_data():
   with sqlite3.connect( GREENHOUSE_DB ) as connection:
      curs = connection.cursor()
      for data_file_number in DATA_FILE_NUMBERS:
         data_file_name = DATA_FILE_BASE + data_file_number + DATA_FILE_EXTENSION
         rows = read_data_from_a_file( data_file_name )
         print( 'read data from datafile', data_file_name )
   return True

def save_this_code_for_a_second():
   for row in reader:
      print( 'Inserting row:', row )   # to see the data
      insert = "INSERT INTO greenhouse(unix_time,temp_1) VALUES (?, ?)"
      curs.execute( insert, row )
   with open( DATA_TEMP_3 ) as data:
      reader = csv.reader( data )
      for row in reader:
         print( 'Inserting row:', row )   # to see the data
         insert = "INSERT INTO greenhouse(unix_time,temp_3) VALUES (?, ?)"
         curs.execute( insert, row )
##
#  Read and return the data in a single .csv file
#
def read_data_from_a_file( data_file_name ):
   print( 'read_data_from_a_file: reading data file "', data_file_name + '"')
   with open( data_file_name ) as data:
       ## reader = csv.reader( data )
       rows = csv.reader( data )
   return rows

##
#  In addition to being a small library of reusable functions,
#     this program can be run on the command line to drop and recreate the db
#
if __name__ == '__main__':
   drop_table()
   create_db()
   seed_data()
