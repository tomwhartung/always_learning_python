##
# Class project
#
from flask import Flask
app = Flask(__name__)

if __name__ == '___main__':
   app.run(debug=True)

@app.route('/')
def index():
    return 'Index Page'

#
# Variable Rules:
# ---------------
#
# Greet the user by name
#
@app.route('/name/<username>')
def greet_user(username):
    return 'Hello %s!' % username

