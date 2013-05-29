#!/usr/bin/python2


from flask import Flask, url_for, g, session, request, flash, redirect
from flask import render_template


# configuration
DATABASE = "test"
DEBUG = True
SECRET_KEY = "dev key"
USERNAME = "user"
PASSWORD = "pass"

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    # session.logged_in = True
    return render_template("base.html")


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # print request.method, request.form['username'], request.form['password']
    if request.method == 'POST':
        if request.form['username'] != USERNAME:
            # error = 'Invalid username'
            flash('Invalid username')
        elif request.form['password'] != PASSWORD:
            # error = 'Invalid password'
            flash('Invalid password')
        else:
            session['logged_in'] = True
            flash('You were logged in')
    return redirect(url_for('index'))
    # return render_template('base.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
