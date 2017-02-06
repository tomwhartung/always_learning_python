##
# Application module for flaskr app
#
# All the imports:
# From Step 2 in the tutorial
#
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

#
# Create the application instance :)
# From Step 2 in the tutorial
#
app = Flask(__name__)
app.config.from_object(__name__) # load config from this file , flaskr.py

#
# Load default config and override config from an environment variable
# From Step 2 in the tutorial
#
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#
# Connect to the db
# From Step 2 in the tutorial
#
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

#
# Opens a new database connection if there is none yet for the current application context.
# From Step 4 in the tutorial
#
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

#
# Closes the database again at the end of the request.
# From Step 4 in the tutorial
#
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
