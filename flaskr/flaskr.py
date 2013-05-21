# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash
import psycopg2
from contextlib import closing

# configuration
DATABASE = "test"
DEBUG = True
SECRET_KEY = "dev key"
USERNAME = "test_user"
PASSWORD = "123"

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
	try:
		conn = psycopg2.connect("dbname='"+DATABASE+"' user='"+USERNAME+"' host='localhost' password='"+PASSWORD+"'")
		return conn
	except:
		print "I am unable to connect to the database"

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql') as f:
			db.cursor().execute(f.read())
			db.commit()


if __name__ == '__main__':
	app.run()