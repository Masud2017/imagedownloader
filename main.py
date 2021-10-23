from src.GoogleDownloader import GoogleDownloader
from src.Environment import Environmet

import logging

logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    google = GoogleDownloader(Query="cat",numberImage=50,folder_path="cat")
    google.download_images()
    logging.info(google.get_url())


    