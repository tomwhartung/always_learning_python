
# Lesson 3 - Homework

Some things to note from the second class, on Tues. Feb. 21, 2017.

## Setup Notes:

Most recently we have been using this virtual environment:

```
. virtualenvs/rp-3-python3_6_flask_bokeh_bette.sh
```

We should be able to re-use it for this assignment.

## Homework Notes:

References:

Link to the assignment:

- https://github.com/realpython/web-dev-for-data-scientists/blob/master/lessons/03-visualization.md

### 1. Review Visualization Lesson

Made a few updates:

- updated to set debug flag, removing cruft that was not working
- updated to print a helpful message if the db is not present
- added GREENHOUSE_DB constant to contain the db name, and moved the db into ../db
- added DATA_TEMP_1 constant to contain the data file name, and moved the file into ../data

Result is in 1-review .

### 2. Add drop_table() Function

This is already done.

### 3. Add air temperature data to the chart

#### Steps (givens):

1. Drop the Database
2. Update the schema in db.py
3. Seed the database
4. Update the route handler
5. Update bokeh - convert to multi-line chart

#### Specifics:

Adding data in data/DataTemp3.dat (realpython web-dev-for-data-scientists repo).

1., 2., 3.:

- Added column temp_3 to contain values read from data file DataTemp3.dat
- Added code to read the data, verified it works using the Sqlite Database Browser

4., 5.:

- New route is: http://127.0.0.1:5000/twolines
- The two batches of data are very similar, so I increased the size of graph and decreased the widths of the lines

Result is in 3-add_air_temp .

### 4. Make the Graph Smoother

Note that for some reason we are missing a file named DataTemp2.dat , otherwise the names are continuous.

Here is a list of the files with their line counts:

```
$ wc -l *
  11786 DataTemp1.dat
  11786 DataTemp3.dat
  11780 DataTemp4.dat
  11786 DataTemp5.dat
  11786 DataTemp6.dat
  11786 DataTemp7.dat
  11786 DataTemp8.dat
  11786 DataTemp9.dat
  11786 DataTemp10.dat
  11767 DataTemp11.dat
  11779 DataTemp12.dat
  11787 DataTemp13.dat
```

Preliminary examination (using grep -n, head, and tail) makes it appear that all files contain data covering the same time period.

Added two routes:

- http://127.0.0.1:5000/all
- http://127.0.0.1:5000/each

It's difficult to determine whether these are accurate and correct without digging into the data.

TODO: dig into the data and ensure these are accurate and correct.

Result is in 4-add_in_all_data .

### 5. Call OMDb API From Flask

#### Installation

Using a new virtual environment: rp_4_bette

```
golpy    # /var/www/always_learning/github/customizations/always_learning_python/
cd 08-real_python_class/2017_02_07-Lesson_2/homework/3-bokeh_quickstart
. env.sh
pip3 freeze > requirements.txt
```

Here is what requirements.txt looks like:

```
$ cat requirements.txt
appdirs==1.4.3
click==6.7
Flask==0.12
itsdangerous==0.24
Jinja2==2.9.5
MarkupSafe==1.0
packaging==16.8
pkg-resources==0.0.0
pyparsing==2.2.0
requests==2.13.0
six==1.10.0
Werkzeug==0.11.15
$
```

Note that we can recreate this environment by running this command:

```
pip3 install -r requirements.txt
```

#### TODO

TODO: Test this technique on jane, to ensure it works.

### 6. Where can I get more data?

Reference:  https://dev.socrata.com/

Holding off on this for now.  (Thinking about the government makes me all twitter-brained these days....)

#### TODO

TODO: Complete this step.

