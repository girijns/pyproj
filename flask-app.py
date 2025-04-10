from flask import Flask, request, jsonify
from app_modules import create_db, return_results

app = Flask(__name__)
coll = create_db()

@app.route("/askdemo", methods=["GET"])
def ask_demo():
    results = return_results(coll)
    return jsonify(results)

@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"

if(__name__ == "__main__"):
    app.run(debug=False)