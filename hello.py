from flask import Flask
from pymongo import Connection

app = Flask(__name__)
conn = Connection('127.0.0.1', 27017)

@app.route("/hello")
def find():
	dbHello = conn['hello']
	
	return dbHello['demo'].find()[0]['message'] + '\n'
	
@app.route('/')
def hello():
	return "Hello World!\n"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
