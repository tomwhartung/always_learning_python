##
#  Main app code to display data in the db
#
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

#
#  Initialize the database:
#  By default, we use sqlite to create it in ./test.db
#
BASE = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE, 'test.db')
DATABSE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + DATABASE_PATH)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABSE_URI
db = SQLAlchemy(app)

import models

##
#  Hello world sanity check:
#
@app.route('/')
def index():
    return 'Hello, world'

##
#  See all data currently in db
#
@app.route('/data')
def data():
    all_data = []
    query = models.Currency.query.all()
    for row in query:
        obj = {
            'exchange': row.exchange,
            'price': row.price,
            'time': row.horah
        }
        all_data.append(obj)
    return jsonify(all_data)

##
#  Get the port from the environment and run the app!
#
port = int(os.environ.get('PORT', 8080))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
