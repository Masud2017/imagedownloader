import logging
import unittest
import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__name__))

sys.path.append(ROOT_DIR+"\src")
from CsvDataRecorderSingleton import CsvDataRecorderSingleton

class CsvDataRecorderSingletonTest(unittest.TestCase):
    def test_csv_recorder_singleton(self):
        singleTonObj = CsvDataRecorderSingleton()
        singleTonObj.count_record_info("data")
        singleTonObj.count_record_info("gender")
        singleTonObj.count_record_info("address")
        self.assertIsInstance(singleTonObj.get_record_row(),type(list()))

if __name__ == "__main__":
    # testable_obj = CsvDataRecorderSingletonTest()
    # testable_obj.test_csv_recorder_singleton()
    unittest.main()
    print("CSVRECORDERSINGLETON test is passed!!")