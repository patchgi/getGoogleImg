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
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}
        req = urllib.request.Request(url = query_url, headers = headers)
        res = urllib.request.urlopen(req)
        html = res.read()
        soup = BeautifulSoup(html, "html.parser")

