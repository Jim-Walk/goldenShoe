from pymongo import MongoClient

def test_db_connection():
    client = MongoClient()
    shoes_db = client.GoldenShoe.shoes
    rec = shoes_db.find_one({'Name': 'Becken Cap'})
    assert len(rec) == 10
