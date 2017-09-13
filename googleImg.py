#!/usr/bin/python3
import threading
import urllib.request, urllib.parse
from bs4 import BeautifulSoup
import os

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
        query = urllib.parse.urlencode({ "tbm": "isch", "q": self.query})
        query_url = "https://www.google.co.jp/search?" + query
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0", }
        req = urllib.request.Request(url = query_url, headers = headers)
        res = urllib.request.urlopen(req)
        html = res.read()
        soup = BeautifulSoup(html, "html.parser")
        #なんかあまりうまくタグを取得できなかった
        img_tags = soup.findAll("img", class_="rg_ic rg_i")
        img_urls = [img_tag.attrs["data-src"] for img_tag in img_tags if "data-src" in img_tag.attrs.keys()]
        print(img_urls)
        if not os.path.isdir(self.query):
            os.makedirs(self.query)
