from model.dataset import DataSet
import time


file_folder = '_'.join([str(i) for i in time.localtime(time.time())][:3])
dir_list = ['2020_7_9']
dataset = DataSet(dir_list)
attr_value = dataset.get_date_stock("2020_7_9", "光大证券", "现手")
print("len:", attr_value)

# 对某一天的所有股票按照交易买卖比进行聚类
