
# Lesson 2

Some things to note from the second class, on Tues. Feb. 7, 2017.

## Setup Notes:

Michael likes to create a separate virtual env for each project.
This seems wasteful (of diskspace) and moreover unnecessary to me at this time so I am sticking with using just the one.

Currently - as of finishing the class, but before starting the homework - we are using the one we created for the first lesson's homework.
To enter this virtual environment, enter the following command:

```
. virtualenvs/rp_1_python3_6_flask_bette.sh
```

## Homework Notes:

References:

Link to the assignment:

- https://github.com/realpython/web-dev-for-data-scientists/blob/master/lessons/02-flask.md#homework

Bokeh Links:

- https://www.blog.pythonlibrary.org/2016/07/27/python-visualization-with-bokeh/
-- Python: Visualization with Bokeh
-- for homework part 2

- http://bokeh.pydata.org/en/latest/docs/user_guide/quickstart.html#userguide-quickstart
-- Bokeh Quickstart
-- for homework part 3

- https://github.com/realpython/flask-bokeh-example/blob/master/tutorial.md
-- Flask Bokeh Basics
-- for homework part 4

### 1. Review

I am actively working on two sites that I am running at home:

- groja.com: a flask site
- seeourminds.com: a django site

So I am going to forego the review at this time.

### 2. Python: Visualization with Bokeh

Reference:

- https://www.blog.pythonlibrary.org/2016/07/27/python-visualization-with-bokeh/

#### Installation

Create a virtual environment based on python3.6 , and add flask and bokeh.
```
golpy    # /var/www/always_learning/github/customizations/always_learning_python/
cd virtualenvs
virtualenv -p /usr/bin/python3.6  rp-2-python3_6_flask_bokeh
pip3 install flask
pip3 install bokeh
```

#### Running the demos

```
golpy    # /var/www/always_learning/github/customizations/always_learning_python/
cd 08-real_python_class/2017_02_07-Lesson_2/homework/2-visualization_with_bokeh
python 1-plot.py
python 2-gridplot.py
```

Running the demos opens the graph in firefox.

### 3. Bokeh Quickstart

Reference:

- http://bokeh.pydata.org/en/latest/docs/user_guide/quickstart.html#userguide-quickstart

#### Installation

#### Notes?

### 4. Flask Bokeh Basics

Reference: https://github.com/realpython/flask-bokeh-example/blob/master/tutorial.md

#### Notes?

### 5. Optional: Learn Html and Css

Relying on previous experience and foregoing this for now.


### 6. Optional: Learn SQL

Relying on previous experience and foregoing this for now.


