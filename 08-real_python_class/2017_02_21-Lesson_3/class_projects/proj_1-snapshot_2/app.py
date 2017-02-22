##
#  Class project 1
#
from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

#  App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def hello():
   return 'Hello'

@app.route("/chart")
def chart():
   # create a chart
   p = figure( plot_width=400, plot_height=400 )
   # add a line renderer
   p.line( [1,2,3,4,5], [6,7,8,9,20], line_width=2 )
   js_resources = INLINE.render_js()
   css_resources = INLINE.render_css()
   script, div = components( p )
   return render_template(
      'chart.html',
      plot_script=script,
      plot_div=div,
      js_resources=js_resources,
      css_resources=css_resources
   )


if __name__ == "__main__":
    app.run()
