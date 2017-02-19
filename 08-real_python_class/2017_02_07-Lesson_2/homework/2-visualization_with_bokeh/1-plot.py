##
#  From:
#     https://www.blog.pythonlibrary.org/2016/07/27/python-visualization-with-bokeh/
#
from bokeh.plotting import figure, output_file, show
 
output_file( "/var/www/always_learning/github/customizations/always_learning_python/08-real_python_class/2017_02_07-Lesson_2/homework/2-visualization_with_bokeh/test.html" )
 
x = range(1, 6)
y = [10, 5, 7, 1, 6]
plot = figure(title='Line example', x_axis_label='x', y_axis_label='y')
plot.line(x, y, legend='Test', line_width=4)
show(plot)

