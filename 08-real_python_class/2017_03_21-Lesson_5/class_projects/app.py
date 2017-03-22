##
#  Main app code to display data in the db
#
import os
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

#
#  Initialize the database:
#  By default, we use sqlite to create it in ./test.db
#  When you set up a database on heroku, it sets the
#     DATABASE_URL environment variable
BASE = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE, 'test.db')
DATABSE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + DATABASE_PATH)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABSE_URI
db = SQLAlchemy(app)

import models

##
#  Hello world sanity check:
#
@app.route('/')
def index():
    return 'Hello, world'

from bokeh.plotting import figure
from bokeh.resources import Inline
from bokeh.embed import components
@app.route('/chart1')
def chart1():
    # prepare some data
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]
    # create a new plot with a title and axis labels
    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
    # add a line renderer with legend and line thickness
    p.line(x, y, legend="Temp.", line_width=2)
    # Add the Bokeh static files
    js_resources = Inline.render_js()
    css_resources = Inline.render_css()
    return render_template( "chart.html",
       plot_script=script,
       plot_div=div,
       js_resources = js_resources,
       css_resources = css_resources
    )

@app.route('/chart')
def chart1():
    # grab some data from db
    x = []
    y = []
    query = models.Currency.price.filter_by(exchange='kraken').all()
    for row in query:
        x.append(row.horah)
        x.append(row.price)
    # create a new plot with a title and axis labels
    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
    # add a line renderer with legend and line thickness
    p.line(x, y, legend="Temp.", line_width=2)
    # Add the Bokeh static files
    js_resources = Inline.render_js()
    css_resources = Inline.render_css()
    return render_template( "chart.html",
       plot_script=script,
       plot_div=div,
       js_resources = js_resources,
       css_resources = css_resources
    )

##
#  See all data currently in db
#
@app.route('/data')
def data():
    all_data = []
    query = models.Currency.query.all()
    for row in query:
        obj = {
            'exchange': row.exchange,
            'price': row.price,
            'time': row.horah
        }
        all_data.append(obj)
    return jsonify(all_data)

def create_chart(data):
    data.sort( key=lambda d:d.horah)
    for row in data:


##
#  Get the port from the environment and run the app!
#
port = int(os.environ.get('PORT', 8080))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
