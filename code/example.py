from flask import Flask
from flask import jsonify


app = Flask(__name__) #Create an instance of the class


@app.route('/welcome/')
def home():
    return "Welcome to the Home page"

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)

@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name

@app.route('/person/')
def person():
    return jsonify({'name':'Dean',
                    'address':'South Africa'})

@app.route('/numbers/')
def print_list():
    return jsonify(list(range(5)))

@app.before_request
def before():
    print("This is executed BEFORE each request.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True) #Run the Flask application on a specific PORT