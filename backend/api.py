from flask import Flask, request
from flask_cors import CORS
from datetime import datetime
import sys
from flask import jsonify
import redis
import os

app = Flask(__name__)

# enable cors for ressource api
CORS(app, resources={r'/api/*': {'origins': '*'}})

REDIS_HOST = os.environ.get("REDIS_HOST")
if(REDIS_HOST == ''):
	REDIS_HOST = 'localhost'

r = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True)

@app.route('/', methods=['GET'])
def hello():
	if request.method == 'GET':
		date = datetime.today()
		print(date.strftime("%d/%m/%Y %H:%M"))
		return "HELLO! url api docs http://127.0.0.1:5000/api/v1"
	
@app.route('/api/v1/alltweet', methods=['GET'])
def getAllTweet():
	if request.method == 'GET':
		timestamps = r.lrange("tweets",0,-1)
		tweets = []
		for timestamp in timestamps:
			tweet = r.hgetall(timestamp)
			dicto = {
				"author": tweet.get("author"),
				"subject": tweet.get("subject"),
				"message": tweet.get("message"),
				"timestamp": timestamp,
			}
			whoLiked = r.hgetall("liked_"+request.args.get('author', '')+":"+timestamp)
			whoretweeted = r.hgetall("retweeted_"+request.args.get('author', '')+":"+timestamp)
			if(len(whoLiked) > 0):
				if(whoLiked['timestamp'] == timestamp and request.args.get('author', '') == whoLiked['author']):
					dicto['liked'] = "true"
			if(len(whoretweeted) > 0):
				if(whoretweeted['timestamp'] == timestamp and request.args.get('author', '') == whoretweeted['author']):
					dicto['retweeted'] = "false"
			tweets.append(dicto)
		return jsonify(tweets,200)

	
@app.route('/api/v1/login', methods=['POST'])
def login():
	if request.method == 'POST':
		data = request.get_json()
		user = r.hgetall(data["email"])
		if(len(user) > 0 and data['password'] == user['password']):
			return jsonify({"username": user['username'], "email": data["email"]},200)
		else:
			return jsonify({"message": "user not found"}, 404)
		
@app.route('/api/v1/register', methods=['POST'])
def signUp():
	if request.method == 'POST':
		data = request.get_json()
		if(r.exists(data["username"])):
			return jsonify({"message": "username already exists"}, 500)
		if(r.exists(data["email"])):
			return jsonify({"message": "email already exists"}, 500)
		userByName = r.hset(
			data["username"],
			mapping={
				"email": data["email"],
				"password": data["password"]
			}
		)
		userByEmail = r.hset(
			data["email"],
			mapping={
				"username": data["username"],
				"password": data["password"]
			}
		)
		if(userByName > 0 and userByEmail > 0):
			return jsonify(r.hgetall(data["username"]),200)
		else:
			return jsonify({"message": "user is not registered"}, 500)
		
@app.route('/api/v1/tweet', methods=['POST'])
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
			r.lpush("tweets", timestamp)
			#list of subject
			r.sadd("subjects", data["subject"])
			# list of tweet for one author
			r.lpush("tweets:"+data['author'], timestamp)
			# list of tweet for one subject
			r.lpush("tweets:"+data["subject"], timestamp)
			return jsonify(r.hgetall(timestamp),200)
		else:
			r.delete(timestamp)
			return jsonify({"message": "tweet has been not registered"}, 500)

@app.route('/api/v1/allsubject', methods=['GET'])
def getAllSubject():
	if request.method == 'GET':
		subjects_set = r.smembers("subjects")
		subjects = []
		for subject in subjects_set:
			subjects.append(subject)
		return jsonify(subjects,200)
	
@app.route('/api/v1/tweetofsubject', methods=['GET'])
def getTweetOfSubject():
    if request.method == 'GET':
        subject = request.args.get('subject', '')
        timestamps = r.lrange("tweets:"+subject,0,-1)
        tweets = []
        for timestamp in timestamps:
            tweet = r.hgetall(timestamp)
            dict = {
                "author": tweet.get("author"),
                "subject": tweet.get("subject"),
                "message": tweet.get("message"),
                "timestamp": timestamp
            }
            whoLiked = r.hgetall("liked_"+request.args.get('author', '')+":"+timestamp)
            whoretweeted = r.hgetall("retweeted_"+request.args.get('author', '')+":"+timestamp)
            if(len(whoLiked) > 0):
                if(whoLiked['timestamp'] == timestamp and request.args.get('author', '') == whoLiked['author']):
                    dict['liked'] = "true"
            if(len(whoretweeted) > 0):
                if(whoretweeted['timestamp'] == timestamp and request.args.get('author', '') == whoretweeted['author']):
                    dict['retweeted'] = "false"
            tweets.append(dict)
        return jsonify(tweets,200)
	
@app.route('/api/v1/like', methods=['GET'])
def like():
	if request.method == 'GET':
		timestamp = request.args.get('timestamp', '')
		username = request.args.get('author', '')
		cmd = r.hset(
			"liked_"+username+":"+timestamp,
			mapping={
				"author": username,
				"timestamp": timestamp
			}
		)
		if(cmd > 0):
			return jsonify(r.hgetall("liked_"+username+":"+timestamp),200)
		else:
			return jsonify({"message":"tweet has been not liked"},500)
	
@app.route('/api/v1/dislike', methods=['GET'])
def dislike():
	if request.method == 'GET':
		timestamp = request.args.get('timestamp', '')
		username = request.args.get('author', '')
		res = r.hgetall("liked_"+username+":"+timestamp)
		if(res['timestamp'] == timestamp and res['author'] == username):
			delete = r.delete("liked_"+username+":"+timestamp)
			if(delete == 1):
				return jsonify({"message":"key delete"},200)
			else:
				return jsonify({"message":"key has been not delete"},500)
			
@app.route('/api/v1/retweet', methods=['GET'])
def retweet():
	if request.method == 'GET':
		timestamp = request.args.get('timestamp', '')
		username = request.args.get('author', '')
		cmd = r.hset(
			"retweeted_"+username+":"+timestamp,
			mapping={
				"author": username,
				"timestamp": timestamp
			}
		)
		if(cmd > 0):
			tweet = r.hgetall(timestamp)
			if(tweet.get("author") != username):
				r.lpush("tweets:"+username, timestamp)
			return jsonify(r.hgetall("retweeted_"+username+":"+timestamp),200)
		else:
			return jsonify({"message": "error retweet!!"},500)
	
@app.route('/api/v1/disretweet', methods=['GET'])
def disretweet():
	if request.method == 'GET':
		timestamp = request.args.get('timestamp', '')
		username = request.args.get('author', '')
		res = r.hgetall("retweeted_"+username+":"+timestamp)
		if(res['timestamp'] == timestamp and res['author'] == username):
			delete = r.delete("retweeted_"+username+":"+timestamp)
			if(res['author'] != r.hgetall(timestamp)['author']):
				delt = r.lrem("tweets:"+username,0,timestamp)
			if(delete == 1):
				return jsonify({"message":"key delete"},200)
			else:
				return jsonify({"message":"key has been not delete"},200)
			
@app.route('/api/v1/search', methods=['GET'])
def search():
	if request.method == 'GET':
		timestamps = []
		if(r.exists("tweets:"+request.args.get('value', ''))):
			timestamps = r.lrange("tweets:"+request.args.get('value', ''),0,-1)
		tweets = []
		for timestamp in timestamps:
			tweet = r.hgetall(timestamp)
			if(tweet.get("author") == request.args.get('value', '') or tweet.get("subject") == request.args.get('value', '')):
				dicto = {
					"author": tweet.get("author"),
					"subject": tweet.get("subject"),
					"message": tweet.get("message"),
					"timestamp": timestamp,
				}
				whoLiked = r.hgetall("liked_"+request.args.get('author', '')+":"+timestamp)
				whoretweeted = r.hgetall("retweeted_"+request.args.get('author', '')+":"+timestamp)
				if(len(whoLiked) > 0):
					if(whoLiked['timestamp'] == timestamp and request.args.get('author', '') == whoLiked['author']):
						dicto['liked'] = "true"
				if(len(whoretweeted) > 0):
					if(whoretweeted['timestamp'] == timestamp and request.args.get('author', '') == whoretweeted['author']):
						dicto['retweeted'] = "false"
				tweets.append(dicto)
		return jsonify(tweets,200)
	
@app.route('/api/v1/mytweet', methods=['GET'])
def mytweet():
	if request.method == 'GET':
		timestamps = []
		if(r.exists("tweets:"+request.args.get('author', ''))):
			timestamps = r.lrange("tweets:"+request.args.get('author', ''),0,-1)
		tweets = []
		for timestamp in timestamps:
			tweet = r.hgetall(timestamp)
			originAuthor = tweet.get("author")
			tweet.update({"author":request.args.get('author', '')})
			if(tweet.get("author") == request.args.get('author', '')):
				dicto = {
					"author": originAuthor,
					"subject": tweet.get("subject"),
					"message": tweet.get("message"),
					"timestamp": timestamp,
				}
				whoLiked = r.hgetall("liked_"+request.args.get('author', '')+":"+timestamp)
				whoretweeted = r.hgetall("retweeted_"+request.args.get('author', '')+":"+timestamp)
				if(len(whoLiked) > 0):
					if(whoLiked['timestamp'] == timestamp and request.args.get('author', '') == whoLiked['author']):
						dicto['liked'] = "true"
				if(len(whoretweeted) > 0):
					if(whoretweeted['timestamp'] == timestamp and request.args.get('author', '') == whoretweeted['author']):
						dicto['retweeted'] = "false"
				tweets.append(dicto)
		return jsonify(tweets,200)


if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == "check_syntax":
			print("Build [ OK ]")
			exit(0)
		else:
			print("Passed argument not supported ! Supported argument : check_syntax")
			exit(1)
	app.run(debug=True, host='0.0.0.0', port=5000)