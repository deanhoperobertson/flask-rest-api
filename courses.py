## Mock Student API
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask import jsonify

app = Flask(__name__)
api = Api(app)

#static database
COURSES= {
  '1': {'name': 'Applied Maths', 'price': 23, 'hours': 20},
  '2': {'name': 'English', 'price': 20, 'hours': 10},
  '3': {'name': 'Coding for Beginners', 'price': 21, 'hours': 2},
  '4': {'name': 'Build an API with Flask', 'price': 22, 'hours': 15},
}

class Courses(Resource):
    def get(self):
        '''
        Returns all the entire database.
        '''
        return COURSES

    def delete(self):
        '''
        Delete a record.
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        args = parser.parse_args()

        if str(args["id"]) in COURSES:
            COURSES.pop(str(args['id']))
            return {'message' : 'Record deleted successfully.'}, 200

        else:
            return "Course not found in database."


    def put(self):
        '''
        Add a record.
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('price', required=True)
        parser.add_argument('hours', required=True)
        args = parser.parse_args()

        record = {'name': str(args['name']), 'price': int(args['id']), 'hours': int(args['id'])},

        #add record to dictionary
        COURSES[str(args['id'])] = record

        return {'message' : 'Record added successfully.'}, 200

# Add URL endpoints
api.add_resource(Courses, '/courses')


if __name__ == '__main__':
    app.run()