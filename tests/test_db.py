from pymongo import MongoClient
from util.db_utils import decrease_stock

def test_db_connection():
    client = MongoClient()
    shoes_db = client.GoldenShoe.shoes
    rec = shoes_db.find_one({'Name': 'Becken Cap'})
    assert len(rec) == 10

def test_decrease_stock():
    client = MongoClient()
    shoes_db = client.GoldenShoe.shoes
    rec = shoes_db.find_one({'ID': 1})
    expected = rec['Stock'] - 1
    decrease_stock(1)
    rec = shoes_db.find_one({'ID': 1})
    assert rec['Stock'] == expected
