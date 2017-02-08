##
# Class project 2: calculator
#
from flask import Flask, jsonify
from flask import render_template
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
def calc_add(operator, num1, num2):
    if operator == 'add':
        solution = num1 + num2
    elif operator == 'subtract':
        solution = num1 - num2
    elif operator == 'multiply':
        solution = num1 * num2
    elif operator == 'divide':
        solution = num1 / num2
    resultList = [
        {'operator': operator },
        {'num1': num1 },
        {'num2': num2 },
        {'solution': solution },
    ]
    return jsonify( results=resultList )
    ## return resultList

