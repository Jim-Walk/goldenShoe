from pymongo import MongoClient
client = MongoClient()

def decrease_stock(shoe_id):
    shoes_c = client.GoldenShoe.shoes
    shoe = shoes_c.find_one({'ID':shoe_id})
    shoes_c.update_one({'ID': shoe['ID']}, {'$set':{'Stock': shoe['Stock']-1}})
