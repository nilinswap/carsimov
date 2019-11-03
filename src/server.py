from flask import Flask, jsonify, render_template, request
import time
import json


app = Flask(__name__)


@app.route("/")
def main():
	return render_template('index.html', reload=time.time())

@app.route("/map")
def map():
	return render_template('map.html', reload=time.time())


@app.route("/api/hi_from_python")
def api_info():
	info = {
		"name": "Pyth"
	}
	return jsonify(info)


@app.route("/api/hi_from_js", methods=['POST'])
def recieve_hi():
	data = request.get_json(force=True)
	message_st = "hi " + data['name'] + ", this is Pyth"
	print(message_st)
	
	message = {
		"message": message_st
	}
	return jsonify(message)


if __name__ == "__main__":
	app.run()