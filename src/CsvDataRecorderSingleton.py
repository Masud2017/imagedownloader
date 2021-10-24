import logging

class CsvDataRecorderSingletonMeta(type):
    _instance = {}
    def __call__(cls, *args, **kwds):
        if cls not in cls._instance:
            instance = super().__call__(*args,**kwds)
            cls._instance[cls] = instance
            return cls._instance[cls]
    
class CsvDataRecorderSingleton(metaclass = CsvDataRecorderSingletonMeta):
    def __init__(self):
        self.__count = [] # The reason behind using double underscore before the count variable to make this variable as private    
        # self.logger = logging()
    
    def count_record_info(self,name_of_cata):
        self.__count.append(name_of_cata)
        
    def get_record_row(self):
        logging.info("This is the string value of the counnt  : {}".format(' '.join(str(e) for e in self.__count)))
        return self.__count