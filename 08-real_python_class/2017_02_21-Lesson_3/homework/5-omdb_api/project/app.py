##
#  Homework project: task 5 for week 3 (see for details, see ../../homework.md)
#  Note:
#     The purpose of this exercise is to get introduced to the requests module
#     So I am removing all bokeh- and database-related code
#
from flask import Flask, render_template
import requests

#  App config.
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

##
#  Hello world sanity check
#
@app.route("/")
def hello():
   return 'Hello'

##
#  Run the app!
#
if __name__ == "__main__":
    app.run()
