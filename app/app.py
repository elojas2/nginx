from flask import Flask, Response
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    res = Response("<p>Hello, World!</p>")
    res.headers["date"] = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    res.headers["content-type"] = "text/html; charset=utf-8"
    res.headers["content-length"] = str(len(res.data))
    res.headers["x-served-from"] = "Flask App"
    return res

@app.route("/nocache")
def nocache():
    res = Response("<p>Hello, no cache!</p>")
    res.headers["date"] = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    res.headers["access-control-allow-origin"] = "*"
    res.headers["access-control-allow-methods"] = "GET, POST, OPTIONS"
    res.headers["access-control-allow-headers"] = "Content-Type"
    res.headers["cache-control"] = "no-store"
    return res 

@app.route("/cache")
def cache():
    res = Response("<p>Hello, cache!</p>")
    res.headers["date"] = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    res.headers["access-control-allow-origin"] = "*"
    res.headers["access-control-allow-methods"] = "GET, POST, OPTIONS"
    res.headers["access-control-allow-headers"] = "Content-Type"
    res.headers["vary"] = "api-key"
    res.headers["cache-control"] = "public, max-age=60"
    return res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
