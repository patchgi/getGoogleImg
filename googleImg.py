#!/usr/bin/python3
import threading, os, random, string
import urllib.request, urllib.parse
from bs4 import BeautifulSoup

class GoogleImg(threading.Thread):
    def __init__(self, _query):
        threading.Thread.__init__(self)
        self.query = _query
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
        img_tags = soup.findAll("img", class_="rg_ic rg_i")
        img_urls = [img_tag.attrs["data-src"] for img_tag in img_tags if "data-src" in img_tag.attrs.keys()]
        dir_name = self.query.replace(" ", "_")
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)

        for img_url in img_urls:
            img = urllib.request.urlopen(img_url)
            path = os.path.join(dir_name, ''.join([random.choice(string.ascii_letters + string.digits) for i in range(15)]) + ".jpg")
            local = open(path, "wb")
            local.write(img.read())
            img.close()
            local.close()

