import pymongo
from pymongo import MongoClient

client = MongoClient()

#create DB called currency_db
db = client['currency_db']

# make collection called currency inside the DB
converted_currencies = db.currency

currency = {
'from':'USD',
'to':'EGP',
'price':17.629999,
}

result = converted_currencies.insert_one(currency)
print result.inserted_id
