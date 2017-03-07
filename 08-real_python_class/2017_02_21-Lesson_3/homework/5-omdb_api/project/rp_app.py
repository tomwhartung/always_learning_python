##
#  Copied and pasted from:
#     https://github.com/realpython/web-dev-for-data-scientists/blob/master/lessons/03-visualization.md
#
from flask import Flask, jsonify
import requests

BASE = 'http://www.omdbapi.com/?t={0}&y=&plot=short&r=json'

app = Flask(__name__)

@app.route('/')
def index():
    movie_name = 'star wars'
    url = BASE.format(movie_name)
    r = requests.get(url)
    json_response = r.json()
    print(json_response)
    return jsonify(json_response)


if __name__ == '__main__':
    app.run(debug=True)

