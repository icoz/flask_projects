#!/usr/bin/python2


from flask import Flask, url_for
from flask import render_template


app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
	return render_template("hello.html", name=name)

@app.route("/path/<path:path>")
def path(path):
	return "Path = %s" % path

@app.route("/int/<int:num>")
def int(num):
	return "Int = %d" % num

@app.route("/test")
def test_urls():
	p = url_for('index') + "<br>"
	p += url_for('path', path='any/where') + "<br>"
	p += url_for('int', num='123') + "<br>"
	return p

if __name__ == "__main__":
	app.run(debug=True)
