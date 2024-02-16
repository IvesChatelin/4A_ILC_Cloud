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



if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == "check_syntax":
			print("Build [ OK ]")
			exit(0)
		else:
			print("Passed argument not supported ! Supported argument : check_syntax")
			exit(1)
	app.run(debug=True)