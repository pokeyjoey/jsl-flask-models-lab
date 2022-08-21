from flask import Flask, jsonify
import psycopg2
from venue import Venue
from category import Category
from venue import Venue

app = Flask(__name__)


@app.route('/venues')
def venues():
    conn = psycopg2.connect(database = 'foursquare_development', user = 'postgres', password = 'postgres')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM venues')
    venues = cursor.fetchall()
    venues_list = [Venue(venue).__dict__ for venue in venues]

    return jsonify(venues_list)

@app.route('/venues/<id>')
def venue(id):
    conn = psycopg2.connect(database = 'foursquare_development', user = 'postgres', password = 'postgres')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM venues where id = %s' % id)
    venue = Venue(cursor.fetchone())

    return jsonify(venue.__dict__)

@app.route('/categories')
def categories():
    conn = psycopg2.connect(database = 'foursquare_development', user = 'postgres', password = 'postgres')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    categories_list = [Category(category).__dict__ for category in categories]

    return jsonify(categories_list)

@app.route('/categories/<name>')
def category(name):
    conn = psycopg2.connect(database = 'foursquare_development', user = 'postgres', password = 'postgres')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories where name = '%s'" % name.capitalize())
    category = Category(cursor.fetchone())

    return jsonify(category.__dict__)

app.run(debug = True)
