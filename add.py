import requests
#import htmlmin
import json
#from bs4 import BeautifulSoup


DATA = [
    {
        'decade': '1970s',
        'artist': 'Speak',
        'song': 'You Light Up My Life',
        'weeksAtOne': 10
    },
    {
        'decade': '1980s',
        'artist': 'Hear',
        'song': 'Physical',
        'weeksAtOne': 10
    },
    {
        'decade': '1990s',
        'artist': 'See',
        'song': 'One Sweet Day',
        'weeksAtOne': 16
    }
]

api = {"apiKey": "PkIWkk_SfpSxuasSNp1ZQPrb73MoJQ1r"}
http_start = "https://api.mongolab.com/api/1/"
http_type = "databases/luz34z/collections/songs"
headers = {"Content-Type": "application/json"}

r = requests.post(http_start+http_type, params=api, headers=headers,data = json.dumps(DATA))
print(r)
