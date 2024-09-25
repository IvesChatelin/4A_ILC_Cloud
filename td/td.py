from flask import Flask, request
import sys
from flask import jsonify
import redis

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
cals = []

@app.route('/', methods=['GET'])
def hello():
	if request.method == 'GET':
		return "HELLO! url api docs http://127.0.0.1:5000/api/cal/ \n\
			http://127.0.0.1:5000/api/cal/addition/a/b/key \n\
			http://127.0.0.1:5000/api/cal/soustraction/a/b/key \n\
			http://127.0.0.1:5000/api/cal/division/a/b/key \n\
			http://127.0.0.1:5000/api/cal/multiplication/a/b/key "
	
@app.route('/api/cal/', methods=['GET'])
def get_result():
	if request.method == 'GET':
		return cals

@app.route('/api/cal/addition/<int:a>/<int:b>/<string:key>', methods=['GET'])
def addition(a,b,key):
	add = a+b
	cal = {key,add}
	map = r.hset("addition",mapping={
		key: add
    })
	return jsonify(r.hgetall("addition"))

@app.route('/api/cal/soustraction/<int:a>/<int:b>/<string:key>', methods=['GET'])
def soustraction(key,a,b):
	sous = a-b
	cal = {key,sous}
	r.hset("soustraction",mapping={
		key: sous
    })
	return jsonify(r.hgetall("soustraction"))

@app.route('/api/cal/division/<int:a>/<int:b>/<string:key>', methods=['GET'])
def division(key,a,b):
	if (b == 0):
		error = {"error": "impossible"}
		return jsonify(error, 400)
	div = a/b
	cal = {key,div}
	map = r.hset("division",mapping={
		key: div
    })
	return jsonify(r.hgetall("division"))

@app.route('/api/cal/multiplication/<int:a>/<int:b>/<string:key>', methods=['GET'])
def multiplication(key,a,b):
	mul = a*b
	cal = {key,mul}
	map = r.hset("multiplication",mapping={
		key: mul
    })
	return jsonify(r.hgetall("multiplication"))
	

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == "check_syntax":
			print("Build [ OK ]")
			exit(0)
		else:
			print("Passed argument not supported ! Supported argument : check_syntax")
			exit(1)
	app.run(debug=True)