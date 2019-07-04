from pymongo import MongoClient
client = MongoClient()

def decrease_stock(shoe_id):
    shoes_c = client.GoldenShoe.shoes
    shoe = shoes_c.find_one({'ID':SHOE_ID})
