from flask import Flask
from flask_restful import Resource, Api
from flask import request

app = Flask(__name__)
api = Api(app)


#in memory data store
items =[]


class Item(Resource):#inherets from Resource class

	#GET method
	def get(sel, name):
		
		# filter func returns iterator, so need next() to return single item.
		# add None so next() doesnt raise error if there are no items
		item = next(filter(lambda x: x["name"]==name, items), None)
		# for item in items:
		# 	if item["name"]==name:
		# 		return item
		return {"item": None}, 200 if item else 404 #return null and 404 (not found) http status code


	#POST Method
	def post(self, name):

		if next(filter(lambda x: x["name"]==name, items), None) is not None:
			return {"message": "An item with name '{}'already exists".format(name)}

		data = request.get_json() #force=True 

		item = {"name": name, "price": data["price"]}
		items.append(item)
		return item, 201 #return item and 201 (created) http status code


class Itemlist(Resource):
	def get(self):
		return {"items": items}


#add class resouce to api and define endpoint (similar to @app.route())
api.add_resource(Item, "/item/<string:name>")
api.add_resource(Itemlist, "/items/")

app.run(port=5001, debug=True)
