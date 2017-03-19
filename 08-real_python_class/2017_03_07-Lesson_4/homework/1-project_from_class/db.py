##
# Class project 1 part 2: sqlite3
# Create db, create table, read in data
#
import sqlite3
import csv
CRYPTOCURRS_DB_NAME = 'cryptocurrs.db'
CRYPTOCURRS_TABLE_NAME = 'cryptocurrs'

def drop_table():
   with sqlite3.connect( CRYPTOCURRS_DB_NAME ) as connection:
      curs = connection.cursor()
      curs.execute( 'DROP TABLE IF EXISTS ' + CRYPTOCURRS_TABLE_NAME )
   return True

def create_db():
   with sqlite3.connect( CRYPTOCURRS_DB_NAME ) as connection:
      curs = connection.cursor()
      create_sql = 'CREATE TABLE ' + CRYPTOCURRS_TABLE_NAME + '('
      create_sql += 'currency TEXT, '
      create_sql += 'price REAL, '
      create_sql += 'hora DATETIME DEFAULT CURRENT_TIMESTAMP)'
      curs.execute( create_sql )
      ## cursor.execute("""INSERT INTO greenhouse VALUES (79.0, )""")
   return True

##
#  Don't worry about seeding data right now
#  (This function is incomplete and untested)
#
def seed_data():
   # open db, open datafile, iterate through datafile, running INSERT
   with sqlite3.connect( CRYPTOCURRS_DB_NAME ) as connection:
      curs = connection.cursor()
      insert = 'INSERT INTO ' + CRYPTOCURRS_TABLE_NAME + ' VALUES ( "bitcoin", )'
      print( 'Inserting row:', row )   # to see the data
      curs.execute( "INSERT INTO greenhouse VALUES (?, ?)", row )

if __name__ == '__main__':
   drop_table()
   create_db()
   ## seed_data()
