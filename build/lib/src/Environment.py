import os
import sys
import yaml
import logging

class Environmet:
    def __init__ (self,file_name):
        self.file_name = file_name
        self.ROOT_DIR = os.path.dirname(os.path.abspath(__name__))

        self.path = os.path.join(self.ROOT_DIR,"application.yml")

        with open(self.path,"r") as file:
            self.yml_data = yaml.load(file,Loader = yaml.FullLoader)
    
     
    def get_key(self,key):
       return self.yml_data[key]