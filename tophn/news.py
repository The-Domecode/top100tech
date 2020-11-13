import requests
from datetime import datetime, timezone
from decouple import config

"""
    print("Title" + ":" + itemresponse['title'])
    print("URL" + ":" + itemresponse['url'])
    print("Time" + ":" + str(time))
    """


def main():

    url = "https://community-hacker-news-v1.p.rapidapi.com/topstories.json"

    querystring = {"print": "pretty"}

    headers = {
        'x-rapidapi-key': config("HN_RAPID_API_KEY"),
        'x-rapidapi-host': "community-hacker-news-v1.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring).json()

    for i in range(50):
        itemurl = ("https://community-hacker-news-v1.p.rapidapi.com/item/" +
                   str(response[i]) + ".json")
        """
        print((str(i+1)+"."), end=" ")
        """
        itemresponse = requests.request(
            "GET", itemurl, headers=headers, params=querystring).json()

        time = datetime.fromtimestamp(
            float(itemresponse['time']), timezone.utc)

        print(itemresponse['title'])
