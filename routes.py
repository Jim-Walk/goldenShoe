from flask import Flask, render_template
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient()

shoes_c = client.GoldenShoe.shoes

@app.route('/')
def hello_world():
    all_shoes = []
    for shoe in shoes_c.find():
        all_shoes += shoe
    return render_template('index.html', all_shoes=all_shoes)

@app.route('/shoe/<int:SHOE_ID>')
def shoe(SHOE_ID):
    shoe = shoes_c.find_one({'ID':SHOE_ID})
    return render_template('shoe.html', shoe=shoe)
