#!flask/bin/python
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
import algorithm
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    j={"status": 4004,"type": "BadResponseException","message": "Resource not entered"}
    return jsonify(j)

@app.route('/<user_name>')
def call_script(user_name=None):
    print(user_name)
    status,v1,v2,v3,v4 = algorithm.main(user_name)
    j={'status':status}
    return jsonify(j,v1,v2,v3,v4)

@app.errorhandler(Exception)
def handle_error(e):
    if isinstance(e, HTTPException):
        code = e.code
        return jsonify({"error":str(e),"status":code}), code


if __name__ == '__main__':
    app.run(debug=True)
