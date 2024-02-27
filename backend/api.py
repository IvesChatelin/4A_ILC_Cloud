from flask import Flask, request
from flask_cors import CORS
from datetime import datetime
from markupsafe import escape
import sys
import pandas as pd
from flask import jsonify
import redis

app = Flask(__name__)

# enable cors for ressource api
CORS(app, resources={r'/api/*': {'origins': '*'}})

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
#key=timestamp, value={“author”: “username”, “tweet”: ”message”, "subject": "subject"}
#key=timestamps, values=[timestamp_1, timestamp_2, timestamp_3]
#key=email, value={"username":"username", "password":"pwd" }
#key=subject, value=[timestamp_1, timestamp_2, timestamp_3]
#key=author, value=[timestamp_1, timestamp_2, timestamp_3]


@app.route('/', methods=['GET'])
def hello():
	if request.method == 'GET':
		date = datetime.today()
		print(date.strftime("%d/%m/%Y %H:%M"))
		return "HELLO! url api docs http://127.0.0.1:5000/api"
	
@app.route('/api/alltweet', methods=['GET'])
def getAllTweet():
	if request.method == 'GET':
		timestamps = r.lrange("tweets",0,-1)
		tweets = []
		for timestamp in timestamps:
			tweet = r.hgetall(timestamp)
			dict = {
				"author": tweet.get("author"),
				"subject": tweet.get("subject"),
				"message": tweet.get("message"),
				"timestamp": timestamp
			}
			tweets.append(dict)
		return jsonify(tweets,200)

	
@app.route('/api/login', methods=['POST'])
def login():
	if request.method == 'POST':
		data = request.get_json()
		user = r.hgetall(data["email"])
		if(len(user) > 0):
			return jsonify({"username": user['username'], "email":data["email"]},200)
		else:
			return jsonify({"message": "user not found"}, 404)
		
@app.route('/api/register', methods=['POST'])
def signUp():
	if request.method == 'POST':
		data = request.get_json()
		user = r.hset(
			data["email"],
			mapping={
				"username": data["username"],
				"password": data["password"]
			}
		)
		if(user > 0):
			return jsonify(r.hgetall(data["email"]),200)
		else:
			return jsonify({"message": "user not register"}, 400)
		
@app.route('/api/tweet', methods=['POST'])
def tweet():
	if request.method == 'POST':
		data = request.get_json()
		date = datetime.today()
		timestamp = date.strftime("%d/%m/%Y %H:%M")
		tweet = r.hset(
			timestamp,
			mapping={
				"author": data["author"],
				"subject": data["subject"],
				"message": data["message"]
			}
		)
		if(tweet > 0):
			# list of tweet
			tweetSet = r.lpush("tweets", timestamp)
			# list of tweet for one author
			userWhoHasTweet = r.lpush(data["author"], timestamp)
			# list of tweet for one subject
			subjectTweeted = r.lpush(data["subject"], timestamp)
			return jsonify({"tweet": r.hgetall(timestamp)},200)
		else:
			return jsonify({"message": "tweet has been not registed"}, 400)


if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == "check_syntax":
			print("Build [ OK ]")
			exit(0)
		else:
			print("Passed argument not supported ! Supported argument : check_syntax")
			exit(1)
	app.run(debug=True, host='0.0.0.0', port=5000)