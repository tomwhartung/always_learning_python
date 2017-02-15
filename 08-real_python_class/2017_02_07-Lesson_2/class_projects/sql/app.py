##
# Class project 3: sqlite3
#
from flask import render_template
import sqlite3

app = Flask(__name__)

if __name__ == '___main__':
   app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

#
# Calculator Fcns
# ---------------
#
# Add two numbers
#
@app.route('/calc/<operator>/<int:num1>/<int:num2>')
def calc(operator, num1, num2):
    if operator == 'add':
        solution = num1 + num2
    elif operator == 'subtract':
        solution = num1 - num2
    elif operator == 'multiply':
        solution = num1 * num2
    elif operator == 'divide':
        solution = num1 / num2
    data = {
        'operator': operator,
        'num1': num1,
        'num2': num2,
        'solution': solution,
    }
    return render_template('calc.html', data=data)

#
# save_the_code so I don't have to re-type it
#
def save_the_code():
    resultList = [
        {'operator': operator },
        {'num1': num1 },
        {'num2': num2 },
        {'solution': solution },
    ]
    return jsonify( results=resultList )
    ## return resultList

