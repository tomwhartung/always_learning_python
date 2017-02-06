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

################################################################################
#
# Mainline code to create the app and load the config, allowing for overrides
# ---------------------------------------------------------------------------
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

################################################################################
#
# View functions
# --------------
#
##
# Index (Home page) view to show entries
# From Step 6 in the tutorial
#
@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)

##
# Page to allow adding a new entry
# Form appears on show entries page when user is logged in
# From Step 6 in the tutorial
#
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

##
# Login page
# From Step 6 in the tutorial
#
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

##
# Logout page
# From Step 6 in the tutorial
#
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

################################################################################
#
# Functions for working with the Database
# ---------------------------------------
#
##
# Connect to the specific database.
# From Step 2 in the tutorial
#
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

##
# Function to initialize the database.
# From Step 5 in the tutorial
#
def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

##
# Command-line command to initialize the database.
# From Step 5 in the tutorial
#
@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialized the database.')

##
# Opens a new database connection if there is none yet for the current application context.
# From Step 4 in the tutorial
#
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

##
# Closes the database again at the end of the request.
# From Step 4 in the tutorial
#
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
