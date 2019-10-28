from flask import Flask, jsonify, render_template, request
import time
import json
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html', reload = time.time())

@app.route("/api/info")
def api_info():
    info = {
       "ip" : "127.0.0.1",
       "hostname" : "everest",
       "description" : "Main server",
       "load" : [ 3.21, 7, 14 ]
    }
    return jsonify(info)

@app.route("/api/hi", methods = ['POST'])
def recieve_hi():
    data = request.get_json(force=True)
    #j = json.loads(request.data)
    #data = request.json()
    #data_ = request.form()
    print(data)
    
    message = {
        "message": "hi hi"
    }
    return jsonify(message)

@app.route("/api/calc")
def add():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    div = 'na'
    if b != 0:
        div = a/b
    return jsonify({
        "a"        :  a,
        "b"        :  b,
        "add"      :  a+b,
        "multiply" :  a*b,
        "subtract" :  a-b,
        "divide"   :  div,
    })



if __name__ == "__main__":
    app.run()