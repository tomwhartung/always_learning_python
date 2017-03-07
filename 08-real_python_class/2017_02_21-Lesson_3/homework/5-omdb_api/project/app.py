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
   print( 'No movie_name specified (in the "/fm" route)')
   movie_name = 'silence%20of%20the%20lambs'
   return find_movie( movie_name )

##
#  Version of "fm" route that accepts a movie_name
#
@app.route( '/fm/<movie_name>' )
def fm_param( movie_name ):
   print( 'movie_name:', movie_name )
   if movie_name == '':                  ## I believe this is unnecessary
      movie_name = 'american gangster'   ## and perhaps overly-paranoid
   return find_movie( movie_name )

##
#  Shared subroutine to find the movie
#
FORMAT_THE_JSON = False
## FORMAT_THE_JSON = True
def find_movie( movie_name ):
   url = BASE.format(movie_name)
   response = requests.get(url)
   json_response = response.json()
   jsonified_response = jsonify(json_response)
   print( 'json_response:', json_response )
   print( 'jsonified_response:', jsonified_response )
   if FORMAT_THE_JSON :
      return jsonified_response
   else:
      return render_template( 'json.html', json_response=json_response )

##
#  Run the app!
#
if __name__ == "__main__":
    app.run()
