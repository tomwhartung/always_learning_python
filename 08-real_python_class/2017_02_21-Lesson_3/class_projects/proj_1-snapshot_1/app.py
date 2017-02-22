##
#  Class project 1
#
from flask import Flask

#  App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def hello():
   return 'Hello'

if __name__ == "__main__":
    app.run()

