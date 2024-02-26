from flask import Flask, request
from flask_cors import CORS
from datetime import datetime
from markupsafe import escape
import sys
import pandas as pd
from flask import jsonify
import redis

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0)
#key=timestamp, value={“author”: “username”, “tweet”: ”message”, "subject": "subject"}
#key=username, value=[timestamp_1, timestamp_2, timestamp_3]
#key=subject, value=[timestamp_1, timestamp_2, timestamp_3]


@app.route('/', methods=['GET'])
def hello():
	if request.method == 'GET':
		date = datetime.today()
		print(date.strftime("%d/%m/%Y %H:%M"))
		return "HELLO! url api docs http://127.0.0.1:5000/api"
	
@app.route('/api/alltweet', methods=['POST'])
def getAllTweet():
	if request.method == 'POST':
		data = request.get_json()
		date = datetime.today()
		key = date.strftime("%d/%m/%Y %H:%M")
		value = {
			"author": data["username"],
			"message": data["message"]
		}
		tweet = {
			
		}
		return "HELLO! url api docs http://127.0.0.1:5000/api"


if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == "check_syntax":
			print("Build [ OK ]")
			exit(0)
		else:
			print("Passed argument not supported ! Supported argument : check_syntax")
			exit(1)
	app.run(debug=True, host='0.0.0.0', port=5000)