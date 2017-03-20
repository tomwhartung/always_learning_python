
# Lesson 4 - Homework

Most important things to note (MITTR) from the fourth class, on Tues. Mar. 7, 2017.

## Setup Notes:

Most recently we have been using this virtual environment:

```
. virtualenvs/rp_5_class_4_bette.sh
```

We should be able to re-use it for this assignment.

## Homework Notes:

References:

Link to the assignment:

- https://github.com/realpython/web-dev-for-data-scientists/blob/master/lessons/04-retrieval.md#homework

## Plan:

0. Create new virtual environment
1. Get the flask-bitcoin-example working locally
2. Migrate any changes I want to make to a new version
3. Ensure my version works locally
4. Ensure I understand how to use sqlalchemy
5. Add sqlalchemy as required
6. Ensure my version still works locally
7. Get my version working on heroku
8. Ensure my version meets all requirements, locally and on heroku

## Step (0): New virtualenv

Reference:

* https://github.com/realpython/web-dev-for-data-scientists/blob/master/lessons/bonus/heroku.md

### 0.1 Create venv

Starting with setting up a virtual environment.

```
cd /var/www/always_learning/github/customizations/always_learning_python/virtualenvs
python3.6 -m venv rp_6_homework_bette
vi rp_6_homework_bette.sh
```

### 0.2 Install

Melding the realpython process with the way I like to do it.

```
cd /var/www/always_learning/github/customizations/always_learning_python/08-real_python_class/2017_03_07-Lesson_4/homework
mkdir 4-homework_1
cd 4-homework_1
l ../3-flask-bitcoin-example/
cp ../3-flask-bitcoin-example/*.* .
cat > env.sh
cat env.sh   ## . /var/www/always_learning/github/customizations/always_learning_python/virtualenvs/rp_6_homework_bette.sh
. env.sh
pip3 install -r requirements.txt     ## NOTE: using pip3!!
```

## Step (1) Get the flask-bitcoin-example working locally

Create a script, `run_locally.sh`, so we don't have to worry about which (if any) of all the different ways of running it actually work.

```
cd /var/www/always_learning/github/customizations/always_learning_python/08-real_python_class/2017_03_07-Lesson_4/homework/4-homework_1
vi run_locally.sh
chmod +x run_locally.sh
cat run_locally.sh
## export FLASK_APP=app.py
## flask run
. env.sh  ## runs the one created above
./run_locally.sh
```

### 1.1 Sanity check

Access in browser:

- http://127.0.0.1:5000/

Seeing 'Hello world.'

### 1.2 `data` route

Access in browser:

- http://127.0.0.1:5000/data

#### 1.2.1 First try:

Getting internal server error (no such table).

```
python -m create_db
```

Created file `4-homework_1/test.db` .

Try again.

#### 1.2.2 Second try:

Getting "[]" (empty list)

Try again.

#### 1.2.3 Third try:

```
python -m seed
```

Now I can see some data!

#### 1.2.4 Play time:

Experimented a bit and I am not understanding a few things:

- Running `python3.6 -m data` does not seem to clear out the data in table
- Not sure how running `python3.6 -m create_db` works:
- Note sure I understand exactly what `from app import db` in create_db.py is doing

## Step (2) Migrate any changes I want to make to a new version

Just keeping this to comments - specifically File and Function headers - for now.

### 2.1 Ideas:

If I had time, or was going to put this into production, I would definitely make these enhancements:

- Move db to a different directory.
- Ensure db is in the gitignore file.
- Create string constants for DB name, etc.
- Ensure variable names "make sense" (e.g., no single-letter variable names, etc.)
- Update function `get_rates()` in data.py to try each service separately rather than fail for all if only one or two fail

### 2.2 Questions:

Don't we need to set the Secret Key?  (Or is that a django thing?)

## Step (3) Ensure my version works locally

It turns out that it "works," but I am not totally understanding the SQLAlchemy part, because I have not yet studied it.

## Step (4) Ensure I understand how to use sqlalchemy

Reference:

- https://github.com/realpython/web-dev-for-data-scientists/blob/master/lessons/bonus/sqlalchemy.md

Looked up a few SQLAlchemy tutorials online:

- http://docs.sqlalchemy.org/en/latest/orm/tutorial.html (Version 1.2 - of SQLAlchemy - NOT the same as Flask-SQLAlchemy!)
- https://www.blog.pythonlibrary.org/2010/02/03/another-step-by-step-sqlalchemy-tutorial-part-1-of-2/ (over 7 years old!)
- https://www.fullstackpython.com/sqlalchemy.html

**NOTE that the version of SQLAlchemy does NOT match the version of Flask-SQLAlchemy!!**
We may want to refer to these later, but should probably look up tutorials Flask-SQLAlchemy instead (NOT the same thing).

## Step (5) Add sqlalchemy as required

Reference: (same as above)

Reviewing the reference, there are several changes to make to the code.

### 5.1 Installing sqlalchemy

Ensure we are in our environment and use **pip3** to install the package

```
. env.sh
pip3 install Flask-SQLAlchemy==2.2     ## NOTE: using pip3!!
```

Looking at `requirements.txt` it appears this should have been installed already.

### 5.2 Updating code

Updating the following files:

- app.py - updated data() at first but it turns out there are no updates needed after all
- models.py - no updates needed
- create_db.py - no updates needed
- data.py - no updates needed (current version contains a for loop not present in example presented on github)

### 5.3 Adding more data

At the end it says to add more data, re-run the server, and see it.

```
python -m seed
```

## Step (6) Ensure my version still works locally

## Step (7) Get my version working on heroku

## Step (8) Ensure my version meets all requirements, locally and on heroku
