# Currency Converter 

this small project is for getting today's changing rate of any currency into EGP (Egyptian Pound) using currency converter 
API http://free.currencyconverterapi.com and Python 2.7.6

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The only thing you need is pymongo DB
```
pip install pymongo
```

## Running

After installing the prerequisites open the terminal and cd into the directory that contains the script


#### Getting the EUR today's price, you can use any currency you want instead of EUR

```
$ python script.py EUR
```
after the previous command the EUR price in EGP have been saved into the DB 


#### Getting all the conversion you have done all the time

```
$ python script.py get_records
```

