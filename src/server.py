from flask import Flask
import flask
app = Flask(__name__)

@app.route("/output")
def output():
	return flask.render_template("index.html", name="Joe")

@app.route('/receiver', methods = ['POST'])
def worker():
	# read json + reply
	data = flask.request.get_json()
	result = ''
	
	print(data)
	for item in data:
		# loop over every row
		result += str(item['make']) + '\n'

	return result

if __name__ == "__main__":
	app.run()