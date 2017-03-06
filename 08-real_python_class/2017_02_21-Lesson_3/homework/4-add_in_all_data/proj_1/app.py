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
   unix_time_1 = []
   temperature_1 = []
   unix_time_3 = []
   temperature_3 = []
   try:
      rows = get_data()
   except:
      return 'Unable to open db. Run db_create.sh to create it and try again.'
   for row in rows:
      date = datetime.datetime.fromtimestamp( row[0] )
      if row[1] != 0.0:
         unix_time_1.append( date )
         temperature_1.append( row[1] )
      elif row[2] != 0.0:
         unix_time_3.append( date )
         temperature_3.append( row[2] )
   plot.multi_line( [unix_time_1,unix_time_3], [temperature_1,temperature_3],
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
   unix_time_1 = []
   temperature_1 = []
   unix_time_3 = []
   temperature_3 = []
   unix_time_4 = []
   temperature_4 = []
   unix_time_5 = []
   temperature_5 = []
   unix_time_6 = []
   temperature_6 = []
   unix_time_7 = []
   temperature_7 = []
   unix_time_8 = []
   temperature_8 = []
   unix_time_9 = []
   temperature_9 = []
   unix_time_10 = []
   temperature_10 = []
   unix_time_11 = []
   temperature_11 = []
   unix_time_12 = []
   temperature_12 = []
   unix_time_13 = []
   temperature_13 = []
   try:
      rows = get_data()
   except:
      return 'Unable to open db. Run db_create.sh to create it and try again.'
   for row in rows:
      date = datetime.datetime.fromtimestamp( row[0] )
      if row[1] != 0.0:
         unix_time_1.append( date )
         temperature_1.append( row[1] )
      elif row[2] != 0.0:
         unix_time_3.append( date )
         temperature_3.append( row[2] )
      elif row[3] != 0.0:
         unix_time_4.append( date )
         temperature_4.append( row[2] )
      elif row[4] != 0.0:
         unix_time_5.append( date )
         temperature_5.append( row[2] )
      elif row[5] != 0.0:
         unix_time_6.append( date )
         temperature_6.append( row[2] )
      elif row[6] != 0.0:
         unix_time_7.append( date )
         temperature_7.append( row[2] )
      elif row[7] != 0.0:
         unix_time_8.append( date )
         temperature_8.append( row[2] )
      elif row[8] != 0.0:
         unix_time_9.append( date )
         temperature_9.append( row[2] )
      elif row[9] != 0.0:
         unix_time_10.append( date )
         temperature_10.append( row[2] )
      elif row[10] != 0.0:
         unix_time_11.append( date )
         temperature_11.append( row[2] )
      elif row[11] != 0.0:
         unix_time_12.append( date )
         temperature_12.append( row[2] )
      elif row[12] != 0.0:
         unix_time_13.append( date )
         temperature_13.append( row[2] )
   ## plot.multi_line( [unix_time_1,unix_time_3], [temperature_1,temperature_3],
   ##     color=["firebrick", "navy"], alpha=[0.8, 0.3], line_width=1 )
   plot.multi_line(
      [unix_time_1,unix_time_3,unix_time_4,unix_time_5,unix_time_6,unix_time_7,unix_time_8,unix_time_9,unix_time_10,unix_time_11,unix_time_12,unix_time_13],
      [temperature_1,temperature_3,temperature_4,temperature_5,temperature_6,temperature_7,temperature_8,temperature_9,temperature_10,temperature_11,temperature_12,temperature_13],
      color=[ "firebrick", "red", "yellow", "orange", "brown", "magenta", "green", "cyan", "lightskyblue", "blue", "navy", "purple"],
      alpha=[0.1, 0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.8, 0.9], line_width=1 )
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
#  Draw a separate chart using each of the datasets
#  First we will try it by brute force.
#  If and when that works, maybe we will get fancy
#
@app.route("/each")
def each():
   # create 12 charts
   plot1 = figure( plot_width=200, plot_height=150, x_axis_type='datetime' )
   plot3 = figure( plot_width=200, plot_height=150, x_axis_type='datetime' )
   plot4 = figure( plot_width=200, plot_height=150, x_axis_type='datetime' )
   plot5 = figure( plot_width=200, plot_height=150, x_axis_type='datetime' )
   plot6 = figure( plot_width=200, plot_height=150, x_axis_type='datetime' )
   plot7 = figure( plot_width=200, plot_height=150, x_axis_type='datetime' )
   plot8 = figure( plot_width=200, plot_height=150, x_axis_type='datetime' )
   plot9 = figure( plot_width=200, plot_height=150, x_axis_type='datetime' )
   plot10 = figure( plot_width=200, plot_height=150, x_axis_type='datetime' )
   plot11 = figure( plot_width=200, plot_height=150, x_axis_type='datetime' )
   plot12 = figure( plot_width=200, plot_height=150, x_axis_type='datetime' )
   plot13 = figure( plot_width=200, plot_height=150, x_axis_type='datetime' )
   unix_time_1 = []
   temperature_1 = []
   unix_time_3 = []
   temperature_3 = []
   unix_time_4 = []
   temperature_4 = []
   unix_time_5 = []
   temperature_5 = []
   unix_time_6 = []
   temperature_6 = []
   unix_time_7 = []
   temperature_7 = []
   unix_time_8 = []
   temperature_8 = []
   unix_time_9 = []
   temperature_9 = []
   unix_time_10 = []
   temperature_10 = []
   unix_time_11 = []
   temperature_11 = []
   unix_time_12 = []
   temperature_12 = []
   unix_time_13 = []
   temperature_13 = []
   try:
      rows = get_data()
   except:
      return 'Unable to open db. Run db_create.sh to create it and try again.'
   for row in rows:
      date = datetime.datetime.fromtimestamp( row[0] )
      if row[1] != 0.0:
         unix_time_1.append( date )
         temperature_1.append( row[1] )
      if row[2] != 0.0:
         unix_time_3.append( date )
         temperature_3.append( row[2] )
      if row[3] != 0.0:
         unix_time_4.append( date )
         temperature_4.append( row[2] )
      if row[4] != 0.0:
         unix_time_5.append( date )
         temperature_5.append( row[2] )
      if row[5] != 0.0:
         unix_time_6.append( date )
         temperature_6.append( row[2] )
      if row[6] != 0.0:
         unix_time_7.append( date )
         temperature_7.append( row[2] )
      if row[7] != 0.0:
         unix_time_8.append( date )
         temperature_8.append( row[2] )
      if row[8] != 0.0:
         unix_time_9.append( date )
         temperature_9.append( row[2] )
      if row[9] != 0.0:
         unix_time_10.append( date )
         temperature_10.append( row[2] )
      if row[10] != 0.0:
         unix_time_11.append( date )
         temperature_11.append( row[2] )
      if row[11] != 0.0:
         unix_time_12.append( date )
         temperature_12.append( row[2] )
      if row[12] != 0.0:
         unix_time_13.append( date )
         temperature_13.append( row[2] )
   plot1.line( unix_time_1, temperature_1 )
   plot3.line( unix_time_3, temperature_3 )
   plot4.line( unix_time_4, temperature_4 )
   plot5.line( unix_time_5, temperature_5 )
   plot6.line( unix_time_6, temperature_6 )
   plot7.line( unix_time_7, temperature_7 )
   plot8.line( unix_time_8, temperature_8 )
   plot9.line( unix_time_9, temperature_9 )
   plot10.line( unix_time_10, temperature_10 )
   plot11.line( unix_time_11, temperature_11 )
   plot12.line( unix_time_12, temperature_12 )
   plot13.line( unix_time_13, temperature_13 )
   js_resources = INLINE.render_js()
   css_resources = INLINE.render_css()
   plot_1_script, plot_1_div = components( plot1 )
   plot_3_script, plot_3_div = components( plot3 )
   plot_4_script, plot_4_div = components( plot4 )
   plot_5_script, plot_5_div = components( plot5 )
   plot_6_script, plot_6_div = components( plot6 )
   plot_7_script, plot_7_div = components( plot7 )
   plot_8_script, plot_8_div = components( plot8 )
   plot_9_script, plot_9_div = components( plot9 )
   plot_10_script, plot_10_div = components( plot10 )
   plot_11_script, plot_11_div = components( plot11 )
   plot_12_script, plot_12_div = components( plot12 )
   plot_13_script, plot_13_div = components( plot13 )
   return render_template(
      'each.html',
      plot_1_script=plot_1_script,
      plot_3_script=plot_3_script,
      plot_4_script=plot_4_script,
      plot_5_script=plot_5_script,
      plot_6_script=plot_6_script,
      plot_7_script=plot_7_script,
      plot_8_script=plot_8_script,
      plot_9_script=plot_9_script,
      plot_10_script=plot_10_script,
      plot_11_script=plot_11_script,
      plot_12_script=plot_12_script,
      plot_13_script=plot_13_script,
      plot_1_div=plot_1_div,
      plot_3_div=plot_3_div,
      plot_4_div=plot_4_div,
      plot_5_div=plot_5_div,
      plot_6_div=plot_6_div,
      plot_7_div=plot_7_div,
      plot_8_div=plot_8_div,
      plot_9_div=plot_9_div,
      plot_10_div=plot_10_div,
      plot_11_div=plot_11_div,
      plot_12_div=plot_12_div,
      plot_13_div=plot_13_div,
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

##
#  Run the app!
#
if __name__ == "__main__":
    app.run()
