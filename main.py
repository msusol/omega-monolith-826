import os
from flask import Flask, send_from_directory

app = Flask(__name__)

WWW_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www")

@app.route("/")
def index():
    return send_from_directory(WWW_ROOT, "index.html")

@app.route("/<path:path>")
def static_proxy(path):
    full = os.path.join(WWW_ROOT, path)
    if os.path.isdir(full):
        path = path.rstrip("/") + "/index.html"
    return send_from_directory(WWW_ROOT, path)

@app.route("/dashboard")
def dashboard():
    return "Dashboard page"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
