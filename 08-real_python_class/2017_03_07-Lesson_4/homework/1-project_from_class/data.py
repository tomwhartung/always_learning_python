##
#  data.py for Class project 1
#
import sqlite3
import requests
from db import CRYPTOCURRS_DB_NAME, CRYPTOCURRS_TABLE_NAME

def get_data():
   resp = requests.get( 'https://www.bitstamp.net/api/v2/ticker/btcusd')
   print( 'get_data returning:', resp.json() )
   return resp.json()

##
#  Insert a row of data into the table
#
def add_data_row( row ):
   with sqlite3.connect( CRYPTOCURRS_DB_NAME ) as connection:
      curs = connection.cursor()
      insert_row = 'INSERT INTO ' + CRYPTOCURRS_TABLE_NAME + ' VALUES ( "bitcoin", )'
      print( 'Inserting row:', row )   # to see the data
      curs.execute( insert_row, row )
      ## curs.execute( "INSERT INTO greenhouse VALUES (?, ?)", row )

##
#  Run the app
#
if __name__ == '__main__':
   row = get_data()
   add_data_row( row )
