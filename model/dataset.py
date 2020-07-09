import time
from collections import defaultdict
import pandas as pd
import os
from model.feature import StocksFeature

# 存放文件的地址
DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../data")

class DataSet(object):
    def __init__(self, dir_list):
        self.dataset = defaultdict()
        self.dir_list = dir_list
        self.prepare_data()
        #self.stock_pool = {}

    def prepare_data(self):
        for date in self.dir_list:
            file_dict = {}
            file_name = os.path.join(DATA_DIR, date)
            for name in os.listdir(file_name):
                # 如果不是要的文件，continue
                if not name.endswith("pandas.csv"):
                    continue
                curr_file_name = os.path.join(file_name, name)
                ctime = os.path.getctime(curr_file_name)
                # print("ctime:", ctime, curr_file_name)
                file_dict[str(ctime)] = curr_file_name
            # 对当前的日期列表进行排序
            sorted(file_dict.items(), key = lambda d: d[0])
            # read to pandas frame
            if len(file_dict.values()) > 0:
                # print("list(file_dict.values())[0]:",list(file_dict.values())[0])
                df = pd.read_csv(list(file_dict.values())[0], sep=",",  encoding = "utf-8")
                df.columns = df.columns.str.replace(' ', '')
                self.dataset[date] = StocksFeature(date_time=date, data_frame=df)
        # 获取日期的数据
        print("date of data list length:", len(self.dataset))

    # 获取某一天的数据
    def get_date_data(self,date):
        if date not in self.dataset.keys():
            return None
        return self.dataset[date]

    def get_date_stock(self, date, stock_name, attr):
        data = self.get_date_data(date)
        if data != None and stock_name in data.stocks.keys():
            return data.stocks[stock_name].attribute[attr]

        return None


# file_folder = '_'.join([str(i) for i in time.localtime(time.time())][:3])
# dir_list = ['2020_7_9']
# dataset = DataSet(dir_list)
# attr_value = dataset.get_date_stock("2020_7_9", "光大证券", "现手")
# print("len:", attr_value)