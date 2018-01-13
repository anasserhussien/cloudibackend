#!/usr/bin/python
# importing required modules

import argparse
import urllib, json
import pymongo
from pymongo import MongoClient
#import pymongo
#from pymongo import MongoClient

# this method for inserting the currency val into DB
def affecting_db(from_currency, to_currency, price):

    client = MongoClient()
    # this gonna make currency_db if it doesn't exist
    db = client['currency_db']

    # this line supposed to make a collection called currency
    currency_collection = db.currency

    # this is the json that should be saved into the database as a document
    currency = {
    'from':from_currency,
    'to':to_currency,
    'price':price,
    }

    # this line should insert the currency into db and get back with obj id
    currency_collection.insert_one(currency)

def get_records_from_db():

    client = MongoClient()
    # this gonna make currency_db if it doesn't exist
    db = client['currency_db']

    # this line supposed to make a collection called currency
    currency_collection = db.currency
    all_doc = currency_collection.find({})
    print 'from|', ' to', ' | ', 'price'
    print '-----------------------------'
    for doc in all_doc:
        print doc['from'],'| ', doc['to'], '| ', doc['price']




# errors and command messages
WELCOME = "Welcome to the currency converter app" +" | enter the currency code to get it converted into EGP"+ " | enter get_records to get the past saved conversions"
HELP = "The currency code consists of 3 CAPITAL letters OR you can enter <get_records> for getting past conversions"
URL = ""

# create a parser object
parser = argparse.ArgumentParser(description = WELCOME )

# add_argument
parser.add_argument("code", nargs = 1, metavar = "argument 1",
                     help = HELP)


# parse the arguments from standard input
args = parser.parse_args()

# check if the argument more than 3 letters
# as any currency code consists of 3 letters only
if len(args.code[0]) != 3:
    # check if the arguments = get_records
    if args.code[0] == "get_records":
        # calling get_records_from_db to get all saved doc in db
        get_records_from_db()
        exit()
    else:
        print HELP
        exit()

# add _EGP part to the entered currency code to convert it into EGP
currency_code = args.code[0] + "_EGP"
# this is the API where we pass the currenc_code and get the json obj
URL = "http://free.currencyconverterapi.com/api/v5/convert?q="+currency_code +"&compact=y&comabct=y"

# read  the json and load into data or show internet connection problem
try:
    response = urllib.urlopen(URL)
    data = json.loads(response.read())
    #print data
except:
    print "Check your internet connection"

# make the currency code uppercase in case the user entered it lower case
currency_code = currency_code.upper()
# check if we got data from the API
# if yes print the price in EGP
# if no that's mean the code entered by user was invalid
if data:
    print "today's %s price is"%args.code[0] , data[currency_code]['val']
    affecting_db(args.code[0].upper(), 'EGP',data[currency_code]['val'])
else:
    print "The currency code you entered is invalid"
