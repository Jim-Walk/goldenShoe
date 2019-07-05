#!/usr/bin/python3

from flask import Flask, render_template
from pymongo import MongoClient
from util.db_utils import decrease_stock
app = Flask(__name__)
client = MongoClient()

shoes_c = client.GoldenShoe.shoes

@app.route('/')
def index():
    all_shoes = []
    for shoe in shoes_c.find():
        all_shoes += [shoe]
    return render_template('index.html', all_shoes=all_shoes)

@app.route('/shoe/<int:SHOE_ID>')
def shoe(SHOE_ID):
    shoe = shoes_c.find_one({'ID':SHOE_ID})
    return render_template('shoe.html', shoe=shoe)

@app.route('/buy/<int:SHOE_ID>')
def buy(SHOE_ID):
    decrease_stock(SHOE_ID)
    return render_template('buy.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
