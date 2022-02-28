from flask import Flask

app = Flask(__name__)

# --- HOME PAGE----
@app.route("/") #decorator to tell Flask what URL should trigger our function.
def home():
	return "Welcome to the Home page"

# --- Request methods ---
app.route("/store", methods=["POST"]) # POST request
def create_store():
	pass


app.route("/store/<string:name>") # GET request
def get_store(name):
	pass


app.route("/store") # GET request
def get_stores():
	pass


app.route("/store/<string:name>/item", methods["POST"]) # POST request
def create_item_in_store(name):
	pass


app.route("/store/<string:name>/item") # GET request
def get_items_in_store(name):
	pass




app.run(port=5000) #run app on specific port