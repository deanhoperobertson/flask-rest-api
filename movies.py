#Books example with Flask
from flask import Flask
from flask import request, jsonify


app = Flask(__name__)

MOVIES = [
    {'id': 0,
     'title': 'Star Wars',
     'director': 'George Lukus',
     'year_released': 2009},
    {'id': 1,
     'title': 'ET',
     'director': 'Spielberg',
     'year_released': 1994},
    {'id': 2,
     'title': 'Titanic',
     'director': 'David Cameron',
     'year_released': 2001}
]

@app.route('/home/', methods=['GET'])
def home():
	return "Welcome to the Movies API home page."


@app.route('/api/v1/movies/all', methods=['GET'])
def api_all():
    return jsonify(MOVIES)


@app.route('/api/v1/movies/select', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])

        ids = [int(movie["id"]) for movie in MOVIES]

        if id not in ids:
        	return "Cannot find that id in movie database."
        else:
        	record = MOVIES[id]
        	return jsonify(record)
    else:
        return "Error: No id field provided. Please specify an id."


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == '__main__':
    app.run()