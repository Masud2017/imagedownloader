import requests
import threading
from BeautifulSoup4 import BeautifulSoup
# from .util.Environment import Environmet
from .Environment import Environmet
import logging
import requests

class GoogleDownloader:
    def __init__(self, Query,numberImage):
        self.env = Environmet("applicaiton.properties")
        self.url = self.env.get_key("url_google")+Query+"&"+self.env.get_key("url_google_last")

    def download_images(self):
        data = requests.get(self.url)
        doc = BeautifulSoup(data, "html.parser")