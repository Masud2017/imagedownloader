from pandas.core.base import DataError
from .CsvDataRecorderSingleton import CsvDataRecorderSingleton
from .Environment import Environmet

import requests
from bs4 import BeautifulSoup
import os
import logging
import requests
import re
import random
from multiprocessing import Process, Lock, cpu_count # This is the mirror of threading module and give more sophisticated controll over mutex locks
import numpy as np
import pandas as pd
import csv

class GoogleDownloader:
    def __init__(self, Query,numberImage,folder_path = "default"):
        self.env = Environmet("applicaiton.yml")
        self.url = self.env.get_key("url_google")+Query+"&"+self.env.get_key("url_google_last")
        self.numberImage = numberImage
        self.folder_path = folder_path
        self.mutex_lock = Lock()
        self.query = Query

    def validate_url(self,url_to_validate):
        if re.search("^https",url_to_validate) or re.search("^http",url_to_validate):
            return True
        return False

    def download_images(self):
        csvRecordSingleton = CsvDataRecorderSingleton() # instance that is responsible to look after of csv rows
        csvRecordSingleton.count_record_info(self.query)

        data = requests.get(self.url)
        bs = BeautifulSoup(data.content,'html.parser')

        # make a record of data catagories that being downloaded
        csv_data = open("data_info.csv","w")
        cv = csv.writer(csv_data)
        cv.writerow(csvRecordSingleton.get_record_row())
        csv_data.close() # close the file pointer after being used
        
        os.system("mkdir {}".format(self.folder_path))

        for img in bs.find_all("img"):
            if 'http' or 'https' in img.get("src"):
                lnk = img.get("src")
                if self.validate_url(lnk) == True:
                    type_of_image = requests.get(lnk).headers["content-type"].split("/")
                    # logging.info(requests.get(lnk).headers["content-disposition"]) # is there any way I can get the name of the image from google ? 
                    with open(self.folder_path+"/"+str(random.random())+"."+type_of_image[1],"wb") as byte_writer:
                        byte_writer.write(requests.get(lnk).content)
                        byte_writer.close()
                else:
                    continue
            else:
                continue

    def get_url(self):
        return self.url

    # def threaded_download(self):
    #     # This is method is identical to the "download_image" method except using thread instead of single thread
    #     # thead = Process(self.download_image,args=())
    #     thread = []
    #     count = cpu_count() # getting the core count of the system cpu.
    #     for _ in count:
    #         thread.append(Process(self.download_images,args=()))
    #     for per_thread in thread:
    #         per_thread.start()

    def convert_to_dataset(self):
        csvRecorderSingleton = CsvDataRecorderSingleton()
        li = csvRecorderSingleton.get_record_row()
        
        return li