from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


#in memory data store
items =[]


class Item(Resource):#inherets from Resource class

	#GET method
	def get(sel, name):
		for item in items:
			if item["name"]==name:
				return item
		return {"item": None}, 404 #return null and 404 (not found) http status code


	def post(self, name):
		item = {"name": name, "price": 12}
		items.append(item)
		return item, 201 #return item and 201 (created) http status code


class Itemlist(Resource):
	def get(self):
		return {"items": items}


#add class resouce to api and define endpoint (similar to @app.route())
api.add_resource(Item, "/item/<string:name>")
api.add_resource(Itemlist, "/items/")

app.run(port=5001, debug=True)
