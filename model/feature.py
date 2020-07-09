import pandas as pd

from xls_utils import STOCK_NAMES

FEATURES = ["名称", "总市值", "时间", "成交", "现手", "代码", "涨幅%",
                         "振幅", "换手"]

FEATURES_NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

INCLUDES = ["名称", "总市值", "时间", "成交", "现手", "代码", "涨幅%",
                         "振幅", "换手"]
# 名称
def func_1(name):
    return name

# 总市值
def func_2(value):
    try:
        return float(value)
    except:
        return 0

# 时间 list
def func_3(value):
    try:
        return value.split(",")
    except:
        return []

# 成交 list
def func_4(value):
    try:
        return value.split(",")
    except:
        return []

# 现手 list 12--,1600↓,0↑,
def func_5(value):
    try:
        return value.split(",")
    except:
        return []

# 代码
def func_6(value):
    return value

# 涨幅%
def func_7(value):
    try:
        v  =  float(value)
        # 如果大于 11% 或者 小于 -11, 返回0
        if v > 11 or v < -11:
            return 0
        return v
    except:
        return 0

# "振幅"
def func_8(value):
    try:
        return float(value[:value.find("%")])
    except:
        return 0

# "换手"
def func_9(value):
    try:
        return float(value[:value.find("%")])
    except:
        return 0


class Feature(object):
    def __init__(self):
        self.attribute = {}

    def add_attribute(self, attr, value):
        self.attribute[attr] = value


class StocksFeature(object):
    def __init__(self, date_time, data_frame):
        self.features = FEATURES
        self.features_nums = FEATURES_NUMS
        assert  len(self.features) == len(self.features_nums)
        self.stocks = {}
        self.date = date_time
        self.preprare_series(data_frame)


    def preprare_series(self, data_frame):
        for index, row in data_frame.iterrows():
            name = row["名称"]
            if name not in self.stocks.keys():
                self.stocks[name] = Feature()
            for index, attr in enumerate(self.features):
                if attr not in INCLUDES:
                    continue
                import sys
                method = getattr(sys.modules[__name__], "func_{}".format(index+1))
                self.stocks[name].add_attribute(attr, method(row[attr]))




