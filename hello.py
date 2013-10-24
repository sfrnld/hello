from flask import Flask
from pymongo import Connection

app = Flask(__name__)
conn = Connection('127.0.0.1', 27017)

@app.route("/hello")
def find():
	dbHello = conn['hello']
	result = []
	
	return dbHello['demo'].find()[0]['message']
	
@app.route('/')
def hello():
	return "Hello World!\n"

if __name__ == "__main__":
	app.run()
