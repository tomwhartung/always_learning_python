##
#  Class project 1
#
from flask import Flask, render_template
import datetime
import sqlite3
import requests

#  App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def hello():
   return 'Hello'

req = requests.get( 'https://www.bitstamp.net/api/v2/ticker/btcusd')

def get_data():
   rows = []
   with sqlite3.connect( 'greenhouse.db' ) as connection:
      curs = connection.cursor()
      curs.execute( 'SELECT * from greenhouse')
      rows = curs.fetchall()
      ## print( 'Calling see_data 1' )
      ## see_data( rows )
   return rows

def see_data( rows ):
   for row in rows:
      print( "row:", row )


if __name__ == "__main__":
    app.run( debug=True )
