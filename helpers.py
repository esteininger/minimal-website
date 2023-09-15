import requests
from datetime import datetime

# medium posts


class Medium:
    def __init__(self, username):
        self.username = username

    def _request(self):
        url = 'https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@{}'.format(
            self.username)
        response = requests.get(url).json()
        return response

    def get(self, limit=10):
        response = self._request()
        l = []
        for item in response['items']:
            d = {
                "title": item['title'],
                "pubDate": datetime.strptime(item['pubDate'], "%Y-%m-%d %H:%M:%S").strftime("%m/%y"),
                "link": item['link'],
                "categories": item['categories']
            }
            l.append(d)
        return l
