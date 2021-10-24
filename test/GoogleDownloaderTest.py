import logging
import unittest
import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__name__))

sys.path.append(ROOT_DIR+"\src")

# from GoogleDownloader import GoogleDownloader
from src.GoogleDownloader import GoogleDownloader

class GoogleDownloaderTest(unittest.TestCase):
    def test_convert_to_dataset(self):
        googleDownloader = GoogleDownloader(Query="cat",numberImage=50,folder_path = "cat")

        self.assertIsInstance(googleDownloader.convert_to_dataset(),type(list()))

        # with self.assertRaises(TypeError):
        #     print("Something went wrong here may be you mistaken in specifiying the type of the excepted data")

if __name__ == "__main__":
    unittest.main()
    print("TestConvertToDataset is passed")