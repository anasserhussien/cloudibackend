#!/usr/bin/python
# importing required modules

import argparse
import urllib, json
#import pymongo
#from pymongo import MongoClient

# errors and command messages
WELCOME = "Welcome to the currency converter app"
HELP = "The currency code consists of 3 CAPITAL letters"
URL = ""

# create a parser object
parser = argparse.ArgumentParser(description = WELCOME )

# add_argument
parser.add_argument("code", nargs = 1, metavar = "Currency_code",
                     help = HELP)


# parse the arguments from standard input
args = parser.parse_args()

# check if the argument more than 3 letters
# as any currency code consists of 3 letters only
if len(args.code[0]) != 3:
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
else:
    print "The currency code you entered is invalid"
