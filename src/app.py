from flask import Flask, jsonify, request
from hello import add

app = Flask(__name__)

@app.get("/")
def index():
    x = int(request.args.get("x", 2))
    y = int(request.args.get("y", 3))
    return jsonify({"ok": True, "sum": add(x, y)})