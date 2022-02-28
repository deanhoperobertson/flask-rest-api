from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

#list of stores
stores =[
	{
		"name": "my special store",
		"items":[
			{
			"name": "my item",
			"price": 15
			}
		]
	}
]

# --- HOME PAGE----
@app.route("/") #decorator to tell Flask what URL should trigger our function.
def home():
	return "Welcome to the Home page"

# --- Request methods ---
@app.route("/store", methods=["POST"]) # POST request
def create_store():
	request_data = request.get_json()

	new_store = {
		"name": request_data["name"],
		"items": []
	}

	stores.append(new_store)
	return jsonify(new_store)


@app.route("/store/<string:name>") # GET request
def get_store(name):
	'''find store and return the store data'''
	
	for store in stores:
		if store["name"] == name:
			return jsonify(store)
	return "Store not found"


@app.route("/store") # GET request
def get_stores():
	return jsonify({'store': stores})


@app.route("/store/<string:name>/item", methods=["POST"]) # POST request
def create_item_in_store(name):
	'''create an item in a store and add to database'''
	request_data = request.get_json()

	for store in stores:
		if store['name'] == name:
			new_item = {
				"name": request_data["name"],
				"price": request_data["price"]
			}

			store["items"].append(new_item)
			return jsonify(new_item)
	return "Store not found"


@app.route("/store/<string:name>/item") # GET request
def get_items_in_store(name):
	'''find store and retuns the items data'''
	for store in stores:
		if store["name"] == name:
			return jsonify(store["items"])
	return "Store not found"



app.run(port=5001) #run app on specific port

