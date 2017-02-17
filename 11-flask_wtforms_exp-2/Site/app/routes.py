##
# From about 1/3 the way down on this page:
#   https://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822
#
from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')
 
if __name__ == '__main__':
  app.run(debug=True)
