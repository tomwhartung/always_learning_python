##
# From flask quickstart:
#   http://flask.pocoo.org/docs/0.12/quickstart/
#
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

