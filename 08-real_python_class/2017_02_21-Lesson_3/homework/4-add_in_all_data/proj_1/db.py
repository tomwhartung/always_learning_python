##
# Class project 1 part 2: sqlite3
# Create db, create table, read in data
#
import sqlite3
import csv
DATA_FILE_BASE = '../data/DataTemp'
DATA_FILE_NUMBERS = ["1", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
DATA_FILE_EXTENSION = '.dat'
GREENHOUSE_DB = '../db/greenhouse.db'
TEMP_COL_NAME_PREFIX = 'temperature_'

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
      for data_file_number in DATA_FILE_NUMBERS:
         schema += ', ' + TEMP_COL_NAME_PREFIX + data_file_number + ' REAL DEFAULT 0'
      schema += ' )'
      curs.execute( schema )
   return True

##
#  Open db and get data from each of the datafiles
#  Iterate through the data running INSERT for each row
#
def seed_data():
   with sqlite3.connect( GREENHOUSE_DB ) as connection:
      curs = connection.cursor()
      for data_file_number in DATA_FILE_NUMBERS:
         data_file_name = DATA_FILE_BASE + data_file_number + DATA_FILE_EXTENSION
         rows = read_data_from_a_file( data_file_name )
         for row in rows:
            temp_column_name = TEMP_COL_NAME_PREFIX + data_file_number
            print( 'Inserting row', row, 'from datafile', data_file_name )
            insert = "INSERT INTO greenhouse(unix_time," + temp_column_name + ")"
            insert += " VALUES (?, ?)"
            curs.execute( insert, row )
   return True

##
#  Read and return the data in a single .csv file
#
def read_data_from_a_file( data_file_name ):
   rows = []
   with open( data_file_name ) as data:
      reader = csv.reader( data )
      for row in reader:
         rows.append( row )
   return rows

##
#  In addition to being a small library of reusable functions,
#     this program can be run on the command line to drop and recreate the db
#  -> This is easily and quickly accomplished by running db_create.sh
#
if __name__ == '__main__':
   drop_table()
   create_db()
   seed_data()
