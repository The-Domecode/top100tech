import requests
from datetime import datetime,timezone
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

	itemresponse = requests.request("GET", itemurl, headers=headers, params=querystring).json()

	print("Title" + ":" + itemresponse['title'])
	print("URL" + ":" + itemresponse['url'])
	time = datetime.fromtimestamp(float(itemresponse['time']),timezone.utc)
	print("Time" + ":" + str(time))	


for i in range(50):
	itemurl =  ("https://community-hacker-news-v1.p.rapidapi.com/item/" + str(response[i]) + ".json")
	print ((str(i)+"."), end = " ")
	item(itemurl)


