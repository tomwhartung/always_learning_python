
# hello_world project

For information about installing django and setting up the required virtual environments, etc. see ../README.md .

## hello_world - about the versions

1. Lightweight Django Book version - does not work - yet (wip)
2. pure_python.py version - works in new virtual environment (see below)
3. startproject versions - created using startproject: there are a few of these online;

This README covers only the first two.

For information about how to use startproject, startapp, etc. see the startproject subdirectory.

### 1. Lightweight Django Book version

See lightweight_django_book.py .

Unable to get this to work, yet (after entering the command, it simply returns).

**WIP (Work in Progress)**

Notes:
* I found several other versions of hello world that use startproject (trying one or more of those next)
* The book is using version 1.8 of django, we are using 1.10 (maybe set up a virtual env using 1.8 and try that?)

### 2. pure_python.py version

#### References:

* http://dfpp.readthedocs.io/en/latest/chapter_01.html   ## where I got the code
* https://pypi.python.org/pypi/six/#downloads            ## where I got the six library
* http://python-future.org/compatible_idioms.html        ## differences between python 2 and 3

#### Setting up the "six" virtual environment

We do not want to always have six installed by default in our environment, so we set up a new one for it:

```
virtualenv --python=`which python` ~/.virtualenvs/six    ## creates the environment
```

Note: I tried specifying "--python=`which python3`" but that kept giving me "Network Unreachable" errors (??).

```
. ~/.virtualenvs/six/bin/activate    ## enter the environment (command saved in enter_six_env.sh for easy reference)
python
>>> import six                       ## gives an error because it is not yet installed in this environment
>>> exit()
goln                                                     ## cd /var/www/learn/
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
mkdir unpack
cp downloads/six-1.10.0.tar.gz unpack
cd unpack
tar -xvzf six-1.10.0.tar.gz
rm six-1.10.0.tar.gz
pip install six-1.10.0
python
>>> import six        ## No error means the setup was successful
>>> exit()
```
#### Running the pure_python.py version

Enter the following commands to start the server and serve the greetings:

```
. ~/.virtualenvs/six/bin/activate                        ## enter the environment (see enter_six_env.sh)
goln                                                     ## cd /var/www/learn/
cd django/github/customizations/always_learning_python   ## I.e. parent dir of this repo
python hello_world/pure_python.py                        ## Access localhost:8000 in browser for "hello" greetins

```

