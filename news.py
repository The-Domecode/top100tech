import requests
import json
from decouple import config

url = "https://community-hacker-news-v1.p.rapidapi.com/topstories.json"

querystring = {"print":"pretty"}

headers = {
    'x-rapidapi-key': config("HN_RAPID_API_KEY"),
    'x-rapidapi-host': "community-hacker-news-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()

def item(url):
	#"https://community-hacker-news-v1.p.rapidapi.com/item/8863.json"

	itemurl = url

	querystring = {"print":"pretty"}

	headers = {
  	  'x-rapidapi-key': config("HN_RAPID_API_KEY"),
    	'x-rapidapi-host': "community-hacker-news-v1.p.rapidapi.com"
    	}

	itemresponse = requests.request("GET", itemurl, headers=headers, params=querystring)

	print(itemresponse.text)


for i in range(100):
	itemurl =  "https://community-hacker-news-v1.p.rapidapi.com/item/" + str(response[i]) + ".json"
	item(itemurl)


