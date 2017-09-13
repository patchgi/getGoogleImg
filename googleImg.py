import threading
import urllib.request
from bs4 import BeautifulSoup

class GoogleImg(threading.Thread):
    def __init__(self, _query, _img_count):
        threading.Thread.__init__(self)
        self.query = _query
        self.img_count = _img_count
        self.page_count = _img_count / 20

    def run(self):
        print("start: " + self.query)
        self.get()
        print("end: " + self.query)

    def get(self):
        query_url = "https://www.google.co.jp/search?tbm=isch&q=" + self.query
        res = urllib.request.urlopen(query_url)
        data = res.read()

