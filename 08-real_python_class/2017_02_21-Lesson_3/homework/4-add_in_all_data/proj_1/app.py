##
#  Class project 1
#
from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
import datetime
import sqlite3
from db import GREENHOUSE_DB


#  App config.
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def hello():
   return 'Hello'

##
#  Draw a chart using a single dataset
#
@app.route("/chart")
def chart():
   # create a chart
   plot = figure( plot_width=400, plot_height=400, x_axis_type='datetime' )
   # add a line renderer
   ## plot.line( [1,2,4,6,7,9], [2,7,4,9,7,3], line_width=2 )
   ## plot.line( [7,5,4,6,7,9], [3,7,4,8,7,8], line_width=4 )
   ## plot.line( [2,5,4,6,7,9], [3,7,4,6,7,8], line_width=4 )
   x = []
   y = []
   try:
      rows = get_data()
   except:
      return 'Unable to open db. Run db_create.sh to create it and try again.'
   ## print( 'Calling see_data 2' )
   ## see_data( rows )
   for row in rows:
      if row[1] != 0.0:
         date = datetime.datetime.fromtimestamp( row[0] )
         x.append( date )
         y.append( row[1] )
   plot.line( x,y )
   js_resources = INLINE.render_js()
   css_resources = INLINE.render_css()
   script, div = components( plot )
   return render_template(
      'chart.html',
      plot_script=script,
      plot_div=div,
      js_resources=js_resources,
      css_resources=css_resources
   )

##
#  Draw a chart using two datasets
#
@app.route("/twolines")
def twolines():
   # create a chart
   plot = figure( plot_width=1000, plot_height=700, x_axis_type='datetime' )
   # add a line renderer
   ## plot.line( [1,2,4,6,7,9], [2,7,4,9,7,3], line_width=2 )
   ## plot.line( [7,5,4,6,7,9], [3,7,4,8,7,8], line_width=4 )
   ## plot.line( [2,5,4,6,7,9], [3,7,4,6,7,8], line_width=4 )
   unix_time_1 = []
   temp_1 = []
   unix_time_3 = []
   temp_3 = []
   try:
      rows = get_data()
   except:
      return 'Unable to open db. Run db_create.sh to create it and try again.'
   ## print( 'Calling see_data 2' )
   ## see_data( rows )
   for row in rows:
      date = datetime.datetime.fromtimestamp( row[0] )
      if row[1] != 0.0:
         unix_time_1.append( date )
         temp_1.append( row[1] )
      if row[2] != 0.0:
         unix_time_3.append( date )
         temp_3.append( row[2] )
   ## plot.line( unix_time_1, temp_1 )
   ## plot.line( unix_time_3, temp_3 )
   plot.multi_line( [unix_time_1,unix_time_3], [temp_1,temp_3],
        color=["firebrick", "navy"], alpha=[0.8, 0.3], line_width=1 )
   js_resources = INLINE.render_js()
   css_resources = INLINE.render_css()
   script, div = components( plot )
   return render_template(
      'chart.html',
      plot_script=script,
      plot_div=div,
      js_resources=js_resources,
      css_resources=css_resources
   )

##
#  Draw a chart using all of the datasets
#
@app.route("/all")
def all():
   # create a chart
   plot = figure( plot_width=1000, plot_height=700, x_axis_type='datetime' )
   # add a line renderer
   ## plot.line( [1,2,4,6,7,9], [2,7,4,9,7,3], line_width=2 )
   ## plot.line( [7,5,4,6,7,9], [3,7,4,8,7,8], line_width=4 )
   ## plot.line( [2,5,4,6,7,9], [3,7,4,6,7,8], line_width=4 )
   unix_time_1 = []
   temp_1 = []
   unix_time_3 = []
   temp_3 = []
   try:
      rows = get_data()
   except:
      return 'Unable to open db. Run db_create.sh to create it and try again.'
   ## print( 'Calling see_data 2' )
   ## see_data( rows )
   for row in rows:
      date = datetime.datetime.fromtimestamp( row[0] )
      if row[1] != 0.0:
         unix_time_1.append( date )
         temp_1.append( row[1] )
      if row[2] != 0.0:
         unix_time_3.append( date )
         temp_3.append( row[2] )
   ## plot.line( unix_time_1, temp_1 )
   ## plot.line( unix_time_3, temp_3 )
   plot.multi_line( [unix_time_1,unix_time_3], [temp_1,temp_3],
        color=["firebrick", "navy"], alpha=[0.8, 0.3], line_width=1 )
   js_resources = INLINE.render_js()
   css_resources = INLINE.render_css()
   script, div = components( plot )
   return render_template(
      'chart.html',
      plot_script=script,
      plot_div=div,
      js_resources=js_resources,
      css_resources=css_resources
   )

##
#  Get all the data
#
def get_data():
   rows = []
   with sqlite3.connect( GREENHOUSE_DB ) as connection:
      curs = connection.cursor()
      curs.execute( 'SELECT * from greenhouse')
      rows = curs.fetchall()
      ## print( 'Calling see_data 1' )
      ## see_data( rows )
   return rows

##
#  Print out the rows retrieved
#
def see_data( rows ):
   for row in rows:
      print( "row:", row )


if __name__ == "__main__":
    app.run()
