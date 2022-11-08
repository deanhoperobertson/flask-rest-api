from fastapi import FastAPI, Request
import os

app = FastAPI()

database =[
	{"Name": "Dean"}
]

USERNAME = os.environ['USER_1']
PASSWORD = os.environ['PASS_1']


@app.get("/")
async def home():
    return "Welcome to the home page!"


@app.get('/data/')
def show():
	return database


@app.get('/new_data/')
def show_secret_data(request: Request):
	username = request.headers.get('username')
	password = request.headers.get('password')

	if all([username, password]):
		if username == USERNAME and password ==PASSWORD:
			return database
		else:
			return 'Credentials are not authorized to view this data.'

	else:
		return 'Missing username and password.'
