from flask import Flask, request, jsonify
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def hello():
    data = {"data": "Hello World"}
    return jsonify(data)
    
if __name__ == '__main__':
    app.run() #(port=8000, debug=True)
    #app.run(debug=True)
    #app.run(host="0.0.0.0", debug=True, port=8080) # use_reloader=False
