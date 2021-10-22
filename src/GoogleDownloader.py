from bs4 import BeautifulSoup
import requests
import threading
from util.Environment import Environmet
import logging
import requests

class GoogleDownloader:
    def __init__(self, Query,numberImage):
        self.env = Environmet("applicaiton.properties")
        self.url = self.env.get_key("url_google")+Query+"&"+self.env.get_key("url_google_last")
    def saveCsv(self):
        data = requests.get(self.url)
        logging.info(data.content)