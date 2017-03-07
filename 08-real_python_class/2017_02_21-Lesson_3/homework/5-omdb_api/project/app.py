##
#  Homework project: task 5 for week 3 (see for details, see ../../homework.md)
#  Note:
#     The purpose of this exercise is to get introduced to the requests module
#     So I am removing all bokeh- and database-related code
#
from flask import Flask, render_template
from flask import jsonify
import requests

BASE = 'http://www.omdbapi.com/?t={0}&y=&plot=short&r=json'

app = Flask(__name__)

##
#  Hello world sanity check
#
@app.route("/")
def hello():
   return 'Hello'

##
#  Code copy-and-pasted from the Real Python version in rp_app.py
#  Except: I am adding a route....
#
@app.route('/find_movie')
def index():
    movie_name = 'star wars'
    url = BASE.format(movie_name)
    r = requests.get(url)
    json_response = r.json()
    print(json_response)
    return jsonify(json_response)

##
#  "fm" is lazy-typists speak for Find Movie
#
@app.route( '/fm' )
def fm():
   movie_name = 'silence of the lambs'
   return find_movie( movie_name )
   ## return myfunc( movie_name )

def myfunc( movie_name ):
   url = BASE.format(movie_name)
   response = requests.get(url)
   json_response = response.json()
   print(json_response)
   return jsonify(json_response)

@app.route( '/fm/<movie_name>' )
def fm_param( movie_name ):
   if movie_name == '':
      movie_name = 'american gangster'
   ## return find_movie( movie_name )
   url = BASE.format(movie_name)
   response = requests.get(url)
   json_response = response.json()
   print(json_response)
   return render_template( 'json.html', json_response=json_response )

def find_movie( movie_name ):
   url = BASE.format(movie_name)
   response = requests.get(url)
   json_response = response.json()
   print(json_response)
   ## return render_template( 'json.html', json_response=json_response )
   return jsonify(json_response)

##
#  Run the app!
#
if __name__ == "__main__":
    app.run()
