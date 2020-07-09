import xlrd
from collections import defaultdict
import pandas
from tqdm import tqdm


STOCK_NAMES = [
'时间', '成交', '现手',
'量比', '现价', '备注', '外盘', '贡献度', 'TTM市盈率', '涨速', '买价', '异动类型', '涨跌', '自选时间', '开盘', '每股盈利', '5日涨幅', '内盘', '实体涨幅', '现均差%', '卖价', '委比%', '10日涨幅', '每股净资产', '最高', '利空', '总手', '年初至今', '振幅', '最低', '主力净量', '总金额', '总市值', '    名称', '20日涨幅', '现手', '代码', '开盘涨幅', '流通市值', '内外比', '金叉个数', '自选收益', '买量', '净利润增长率', '笔数', '涨幅%', '流通比例', '机构动向', '利润总额', '昨收', '流通股本', '自选价格', '散户数量', '细分行业', '净利润?', '总股本', '市净率', '换手', '卖量', '利好', '所属行业'
]
def read_file(filename):
    workbook = xlrd.open_workbook(filename, encoding_override="utf-8") # encoding= utf-8

    table = workbook.sheet_by_index(0)
    nrows = table.nrows
    ncols = table.ncols

    print("nrows：",nrows)
    table_content = []
    for i in range(nrows):
        print(table.row_values(i))
        table_content.append(table.row_values(i))

    return table_content

def pd_read_file(filename):
    import os
    if not os.path.exists(filename):
        raise ("file %s not found"%filename)

    table_content = []
    with open(filename) as f:
        table_content = f.readlines()


    #table_content = pandas.read_excel(filename, encoding="utf-8")
    return table_content

class stock(object):
    def __init__(self):
        self.attribute = defaultdict(str)

    def add_attribute(self, atrr, value):
        self.attribute[atrr] = value

    def get_columns(self):
        return self.attribute.keys()

class stock_union(object):
    def __init__(self, filename):
        self.stock_pool = []

        table = pd_read_file(filename)
        attrs_name = table[0].split('\t')

        for i in range(1, len(table)):
            values = table[i].split('\t')
            item = stock()
            for attr, value in zip(attrs_name,values):
                item.add_attribute(attr, value)

            self.stock_pool.append(item)

    def get_stock_list(self):
        return self.stock_pool


def get_stocks(file_path):
    stocks = stock_union(file_path)
    return stocks.get_stock_list()


# for line in table_content[1:]:
#     for attr, value in zip(table_content[0].split('\t'), line.split('\t')):
#         print(attr, ":", value)
#     break
# print(table_content)
# table_content = pd_read_file("D:\\daytime_data\\2020_7_9\\ratio.xls")
# stocks = get_stocks("D:/daytime_data/2020_7_9/3_33_23.xls")
# from collections import defaultdict
#
# new_stocks = []
# for i in range(len(stocks)):
#     data_list = defaultdict(list)
#     for line in table_content[1:]:
#         for attr, value in zip(table_content[0].split('\t'), line.split('\t')):
#             data_list[attr].append(value)
#
#     print(stocks[i].attribute)
#
#     for key in ["时间","成交", "现手"]:
#         stocks[i].attribute[key] = ",".join(data_list[key])
#
#     break
#
#
# print(stocks[0].attribute)
