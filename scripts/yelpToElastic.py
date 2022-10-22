import json
import boto3
import datetime
import requests
from decimal import *
from time import sleep
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth


region = 'us-east-1'
service = 'es'
credential = boto3.Session(aws_access_key_id="",
                          aws_secret_access_key="", 
                          region_name="us-east-1").get_credentials()
auth = AWS4Auth(credential.access_key, credential.secret_key, region, service)


esEndPoint = ''

es = Elasticsearch(
    hosts = [{'host': esEndPoint, 'port': 443}],
    http_auth = auth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

restaurants = {}
def addItems(data, cuisine):
    for rec in data:
            dataToAdd = {}
            try:
                if rec["alias"] in restaurants:
                    continue;
                dataToAdd['cuisine'] = cuisine
                dataToAdd['RestaurantID'] = str(rec["id"])
                sleep(0.001)
                print(dataToAdd)
                es.index(index="restaurants", doc_type="Restaurant", body=dataToAdd)
            except Exception as e:
                print(e)

cuisines = ['Indian', 'Chinese', 'Italian', 'Continental', 'Mediterranean']
headers = {'Authorization': 'Bearer '}

DEFAULT_LOCATION = 'Brooklyn'
for cuisine in cuisines:
    for i in range(0, 1000, 50):
        params = {'location': DEFAULT_LOCATION, 'offset': i, 'limit': 50, 'term': cuisine + " restaurants"}
        response = requests.get("https://api.yelp.com/v3/businesses/search", headers = headers, params=params)
        js = response.json()
        #print(js["businesses"])
        addItems(js["businesses"], cuisine)

DEFAULT_LOCATION = 'Queens'
for cuisine in cuisines:
    for i in range(0, 1000, 50):
        params = {'location': DEFAULT_LOCATION, 'offset': i, 'limit': 50, 'term': cuisine + " restaurants"}
        response = requests.get("https://api.yelp.com/v3/businesses/search", headers = headers, params=params)
        js = response.json()
        #print(js["businesses"])
        addItems(js["businesses"], cuisine)

DEFAULT_LOCATION = 'Staten Island'
for cuisine in cuisines:
    for i in range(0, 1000, 50):
        params = {'location': DEFAULT_LOCATION, 'offset': i, 'limit': 50, 'term': cuisine + " restaurants"}
        response = requests.get("https://api.yelp.com/v3/businesses/search", headers = headers, params=params)
        js = response.json()
        #print(js["businesses"])
        addItems(js["businesses"], cuisine)

DEFAULT_LOCATION = 'Manhattan'
for cuisine in cuisines:
    for i in range(0, 1000, 50):
        params = {'location': DEFAULT_LOCATION, 'offset': i, 'limit': 50, 'term': cuisine + " restaurants"}
        response = requests.get("https://api.yelp.com/v3/businesses/search", headers = headers, params=params)
        js = response.json()
        #print(js["businesses"])
        addItems(js["businesses"], cuisine)

DEFAULT_LOCATION = 'Bronx'
for cuisine in cuisines:
    for i in range(0, 1000, 50):
        params = {'location': DEFAULT_LOCATION, 'offset': i, 'limit': 50, 'term': cuisine + " restaurants"}
        response = requests.get("https://api.yelp.com/v3/businesses/search", headers = headers, params=params)
        js = response.json()
        #print(js["businesses"])
        addItems(js["businesses"], cuisine)
        
DEFAULT_LOCATION = 'Philadelphia'
for cuisine in cuisines:
    for i in range(0, 1000, 50):
        params = {'location': DEFAULT_LOCATION, 'offset': i, 'limit': 50, 'term': cuisine + " restaurants"}
        response = requests.get("https://api.yelp.com/v3/businesses/search", headers = headers, params=params)
        js = response.json()
        #print(js["businesses"])
        addItems(js["businesses"], cuisine)
        
DEFAULT_LOCATION = 'San Francisco'
for cuisine in cuisines:
    for i in range(0, 1000, 50):
        params = {'location': DEFAULT_LOCATION, 'offset': i, 'limit': 50, 'term': cuisine + " restaurants"}
        response = requests.get("https://api.yelp.com/v3/businesses/search", headers = headers, params=params)
        js = response.json()
        #print(js["businesses"])
        addItems(js["businesses"], cuisine)