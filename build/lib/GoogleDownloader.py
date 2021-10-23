from bs4.element import CharsetMetaAttributeValue
import requests
import threading
from bs4 import BeautifulSoup

from .Environment import Environmet
import logging
import requests

class GoogleDownloader:
    def __init__(self, Query,numberImage):
        self.env = Environmet("applicaiton.properties")
        self.url = self.env.get_key("url_google")+Query+"&"+self.env.get_key("url_google_last")

    def download_images(self):
        data = requests.get(self.url)
        bs = BeautifulSoup(data.content,'html.parser')
        print(bs.body.find("img"))
        # print(type(bs))
        # with open("log.txt","wb") as file:
        #     file.write(bs)

        # file.close()
    def get_url(self):
        return self.url