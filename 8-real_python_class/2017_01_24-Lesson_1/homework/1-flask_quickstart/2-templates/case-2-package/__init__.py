##
# From flask quickstart:
#   http://flask.pocoo.org/docs/0.12/quickstart/
#
#  Rendering Templates - Case 1: a module
#
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

