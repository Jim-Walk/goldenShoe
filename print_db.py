#!/usr/bin/python3
from pymongo import MongoClient

def print_db():
    client = MongoClient()
    shoes_c = client.GoldenShoe.shoes
    for shoe in shoes_c.find():
        for key in shoe:
            print(key, ': ', shoe[key])

if __name__ == '__main__':
    print_db()
