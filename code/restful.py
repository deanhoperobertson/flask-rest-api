from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Student(Resource):#inherets from Resource class

	#GET method
	def get(sel, name):
		return {"student" : name}

#add class resouce to api and define endpoint (similar to @app.route())
api.add_resource(Student, "/student/<string:name>")


app.run(port=5001)
