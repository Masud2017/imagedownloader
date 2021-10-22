from src.GoogleDownloader import GoogleDownloader
from src.util.Environment import Environmet

import logging

logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    # env = Environmet("application.yml")
    # # env.get_key(key = "hello")
    # print("hello world")
    # # print("Pringting the data : ",env.get_key(key="server.port")
    # data = env.get_key(key = "server.port")

    google = GoogleDownloader(Query="dog",numberImage=50)
    google.saveCsv()


    