##
#  Routines to support accessing the sqlite3 table (db) named NameEmail
#  By default (when run on the command line) this program prints all rows
#  Reference for Flask DB patterns:
#     http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
#
import sqlite3
DB_DIRECTORY = '../db/'
NAME_EMAIL_TABLE = DB_DIRECTORY + 'NameEmail.db'

################################################################################
## #
## #  Note: we know, this file has no routes!
## #  However, we import and declare app so we can use it to call open_resource
## #  (and maybe more later)
## #
## from flask import Flask
## app = Flask(__name__)

################################################################################
#  Functions:
#  ----------
#  The idea is to import only the functions you need to get the job done
#
##
#  Insert a row into the table
#
def insert_name_email( name, email, consulting=0, newsletter=0, portrait=0 ):
   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
      curs = connection.cursor()
      ## cur.execute("INSERT INTO account_holder (email,username,phone,password) VALUES (?,?,?,?)", (email,username,phone,password))
      curs.execute(
         "INSERT INTO NameEmail (name,email,consulting,newsletter,portrait) VALUES (?,?,?,?,?)",
            ( name, email, consulting, newsletter, portrait ) )
   return True

##
#  Insert a row of hard-coded values into the table
#  We wrote this before the above (general) function and are keeping it (for now)
#     because it might come in handy for debugging the general function someday.
#  Absolutely this is cruft and can be deleted, if desired!
#
def insert_hard_coded_name_email():
   with sqlite3.connect( NAME_EMAIL_TABLE ) as connection:
      curs = connection.cursor()
      curs.execute(
         "INSERT INTO NameEmail (name,email,date_added,date_changed) VALUES (?,?,?,?)",
            ( 'Sam', 'sam@sam.com', 1487894885, 1487894885 ) )
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
   print_table()
