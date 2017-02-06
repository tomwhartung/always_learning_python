##
# From flask quickstart:
#   http://flask.pocoo.org/docs/0.12/quickstart/
#
#  Rendering Templates - Case 1: a module
#
from flask import Flask
from flask import request
from flask import make_response
from flask import render_template

app = Flask(__name__)

##
#   If we get a name in the url,
#       use that as the name
#       set it in a cookie
#   else
#       if the name is set in the cookie
#           use the name in the cookie
#       else
#           user is anonymous
#
#   A value of 'unset??' means there is a logic error
#
def try_to_get_cookie( url_name='' ):
    users_name = 'unset??'
    if url_name == '':
        try:
            users_name = request.cookies.get( 'users_name' )
        except:
            users_name = 'Anonymous'
        return render_template( 'index.html', name=users_name )
    else:
        users_name = url_name
        response = make_response(render_template( 'index.html', name=users_name) )
        response.set_cookie( 'users_name', users_name )
        return response

@app.route('/')
@app.route('/<url_name>')
def index(url_name=''):
    return try_to_get_cookie( url_name )

@app.route('/hello/')
@app.route('/hello/<url_name>')
def hello(url_name=''):
    return try_to_get_cookie( url_name )

