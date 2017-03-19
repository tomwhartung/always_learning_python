
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
3. Get my version working locally
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

Access in browser:

- http://127.0.0.1:5000/

Seeing 'hello world.'


## Step (2) Migrate any changes I want to make to a new version

## Step (3) Get my version working locally

