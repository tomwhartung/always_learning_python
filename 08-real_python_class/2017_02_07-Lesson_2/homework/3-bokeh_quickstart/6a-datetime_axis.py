##
#  Preparation for sixth example from:
#     http://bokeh.pydata.org/en/latest/docs/user_guide/quickstart.html#userguide-quickstart
#  Running the example, I got this error:
#     RuntimeError: bokeh sample data directory does not exist, please execute bokeh.sampledata.download()
#  -> Run this program to fix the error.
#
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata import download

download()
