from .Environment import Environmet

from bs4.element import CharsetMetaAttributeValue
import requests
import threading
from bs4 import BeautifulSoup
import os
import logging
import requests
import re
import random
import sys

class GoogleDownloader:
    def __init__(self, Query,numberImage,folder_path = "default"):
        self.env = Environmet("applicaiton.properties")
        self.url = self.env.get_key("url_google")+Query+"&"+self.env.get_key("url_google_last")
        self.numberImage = numberImage
        self.folder_path = folder_path

    def validate_url(self,url_to_validate):
        if re.search("^https",url_to_validate) or re.search("^http",url_to_validate):
            return True
        return False

    def download_images(self):
        data = requests.get(self.url)
        bs = BeautifulSoup(data.content,'html.parser')
        
        os.system("mkdir {}".format(self.folder_path))

        for img in bs.find_all("img"):
            if 'http' or 'https' in img.get("src"):
                lnk = img.get("src")
                if self.validate_url(lnk) == True:
                    type_of_image = requests.get(lnk).headers["content-type"].split("/")

                    with open(self.folder_path+"/"+str(random.random())+"."+type_of_image[1],"wb") as byte_writer:
                        byte_writer.write(requests.get(lnk).content)
                        byte_writer.close()
                else:
                    continue
            else:
                continue
    def get_url(self):
        return self.url