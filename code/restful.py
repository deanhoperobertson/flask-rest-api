from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask_jwt import JWT, jwt_required

from security import authenticate, indentity

app = Flask(__name__)
app.secret_key = 'dean'
api = Api(app)

'''
this function creates a new endpoint /auth
which processing the credentials and returns
an encoded JW token
'''
jwt = JWT(app, authenticate, indentity)

#in memory data store
items =[]


class Item(Resource):#inherets from Resource class

	#decorator
	@jwt_required()
	def get(self, name):
		
		# filter func returns iterator, so need next() to return single item.
		# add None so next() doesnt raise error if there are no items
		item = next(filter(lambda x: x["name"]==name, items), None)
		# for item in items:
		# 	if item["name"]==name:
		# 		return item
		return {"item": item}, 200 if item else 404 #return null and 404 (not found) http status code


	#POST Method
	def post(self, name):

		if next(filter(lambda x: x["name"]==name, items), None) is not None:
			return {"message": "An item with name '{}'already exists".format(name)}

		data = request.get_json() #force=True 

		item = {"name": name, "price": data["price"]}
		items.append(item)
		return item, 201 #return item and 201 (created) http status code


	def delete (self, name):
		global items
		items = list(filter( x: x['name'] != name, items))
		return {'message': 'Item deleted'}



class Itemlist(Resource):
	def get(self):
		return {"items": items}


#add class resource to api and define endpoint (similar to @app.route())
api.add_resource(Item, "/item/<string:name>")
api.add_resource(Itemlist, "/items/")

app.run(port=5001, debug=True)
