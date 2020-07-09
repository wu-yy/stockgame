import os
import time
import pyautogui
import pandas as pd
from xls_utils import stock_union, stock, STOCK_NAMES, pd_read_file, get_stocks
import pandas as pd

def open_stock_software():
    #os.popen('C:\同花顺软件\同花顺\hexin.exe')
    # pyautogui.moveTo(451, 1060, duration=1)
    # pyautogui.click(451, 1060)
    # login
    pyautogui.moveTo(593, 511, duration=4)
    pyautogui.click(593, 511)

    time.sleep(15)

    # 激活当前窗口
    pyautogui.moveTo(800, 5, duration=4)
    pyautogui.click(800, 5)
    time.sleep(15)

    # 点击个股
    pyautogui.moveTo(944, 54, duration=4)
    pyautogui.click(944, 54)
    pyautogui.click(944, 54)
    time.sleep(10)

    # 鼠标移动到第一行
    pyautogui.moveTo(191, 120, duration=4)
    #pyautogui.click(191, 120)
    time.sleep(10)


    return

    time.sleep(15)
    pyautogui.moveTo(1352, 52, duration=4)
    pyautogui.click(1352, 52)
    time.sleep(15)

    pyautogui.moveTo(533, 79, duration=1)
    pyautogui.click(533, 79)
    time.sleep(10)

    n = 100

    while (n > 0):
        n -= 1
        pyautogui.scroll(1)
        time.sleep(5)
    h, w = pyautogui.size()
    pyautogui.moveTo(h / 2, w / 2, duration=1)



def download_data_once(file_folder):
    #n = 10
    #while (n > 0):
    #    pyautogui.scroll(1)
    #    n -= 1
    #    time.sleep(1)
    # 鼠标移动到第一行
    x0 = 191
    y0 = 120
    pyautogui.moveTo(x0, y0, duration=1)
    pyautogui.click(x0, y0,button='right')
    time.sleep(2)

    # 移动到数据导出
    pyautogui.moveTo(x0+100,y0+230, duration=1)

    # 移动到导出当前数据并点击
    pyautogui.moveTo(x0+100+150, y0+230, duration=1)
    pyautogui.click(x0+100+150, y0+230)

    # 移动到输入框
    pyautogui.moveTo(617, 270, duration=1)
    pyautogui.click(617,270)

    #ctl a
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')

    pyautogui.typewrite(["backspace"])

    hour, miniute, sec = time.localtime(time.time())[3:6]
    save_file_name = "D:\daytime_data\\" + file_folder + '\\' + "{}_{}_{}".format(hour, miniute, sec) + ".xls"
    pyautogui.typewrite(save_file_name)

    #下一步
    pyautogui.moveTo(797,515, duration=1)
    pyautogui.click(797, 515)
    pyautogui.sleep(1)

    # 下一步
    pyautogui.click(797, 515)
    pyautogui.sleep(14)

    #完成
    pyautogui.click(797, 515)
    pyautogui.sleep(4)

    pyautogui.click(797, 515)

    pyautogui.sleep(10)
    pyautogui.click(797, 515)

    if not os.path.exists(save_file_name):
        raise ("FILE{} is not exits!".format(save_file_name))


    return save_file_name


def get_ratio(save_file_name, file_folder):
    # 移动到第一行
    pyautogui.moveTo(195, 122, duration=1)
    pyautogui.doubleClick(195, 122)




    file_ctime = 0
    ratio_file_name = "D:\daytime_data\\" + file_folder + '\\' + "ratio" + ".xls"

    if os.path.exists(ratio_file_name):
        file_ctime = os.path.getmtime(ratio_file_name)
    print("first time:", file_ctime)

    #pyautogui.typewrite(save_file_name)
    stocks = get_stocks(save_file_name)
    number = 0
    for i in range(len(stocks)):
        hour, miniute, sec = time.localtime(time.time())[3:6]
        if miniute % 10 == 0:
            # 保持网络畅通
            result = ping()

        if number >= 1000:
            break
        number+=1

        # click ratio
        pyautogui.moveTo(1216, 260, duration=0.5)
        pyautogui.doubleClick(1216, 620)
        # center
        x0 = 400
        y0 = 400
        pyautogui.moveTo(400, 400, duration=0.5)
        pyautogui.click(400, 400, button="right")

        # exports data

        pyautogui.moveTo(x0 + 100, y0 + 164, duration=0.5)
        pyautogui.moveTo(x0 + 100 + 160, y0 + 164, duration=0.5)
        pyautogui.click(x0 + 100 + 160, y0 + 164)

        # 移动到输入框
        pyautogui.moveTo(617, 270, duration=0.5)
        pyautogui.click(617, 270)

        # ctl a
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.keyUp('ctrl')

        pyautogui.typewrite(["backspace"])

        pyautogui.typewrite(ratio_file_name)

        # 下一步
        pyautogui.moveTo(797, 515, duration=0.5)
        pyautogui.click(797, 515)
        pyautogui.sleep(0.5)

        # 下一步
        pyautogui.click(797, 515)
        pyautogui.sleep(2)

        # 完成
        pyautogui.click(797, 515)
        pyautogui.sleep(0.5)

        print("sec filetime:",file_ctime)
        if not os.path.exists(ratio_file_name):
            print("not exist ratio file")
            break
        elif os.path.getmtime(ratio_file_name) == file_ctime:
            print("file_time is old:", os.path.getmtime(ratio_file_name), ", ",file_ctime)
            break
        else:
            file_ctime = os.path.getmtime(ratio_file_name)

        table_content = pd_read_file(ratio_file_name)

        from collections import defaultdict
        data_list = defaultdict(list)
        for line in table_content[1:]:
            for attr, value in zip(table_content[0].split('\t'), line.split('\t')):
                data_list[attr].append(value)

        for key in ["时间","成交", "现手"]:
            stocks[i].add_attribute(key, ",".join(data_list[key]))
            # print(data_list[key])

        # back
        pyautogui.moveTo(68, 44, duration=0.5)
        pyautogui.click(68,44)
        pyautogui.sleep(0.5)

        # next
        pyautogui.moveTo(107, 56,duration=0.5)
        pyautogui.click(107,56)
        pyautogui.sleep(2)


    # save pandas to file
    row_list = []
    for row in stocks:
        dict1 = defaultdict(str)
        for name in STOCK_NAMES:
            dict1[name] = row.attribute[name]
        row_list.append(dict1)
    data_frame = pd.DataFrame(row_list)

    save_pandas_file = save_file_name.split('.')[0]+"_pandas.csv"
    data_frame.to_csv(save_pandas_file, sep=",")
    return


def close_software():
    pyautogui.moveTo(1345, 17, duration=4)
    pyautogui.click(1345, 17)


def ping():
    result = os.system(u"ping www.baidu.com")
    # result = os.system(u"ping www.baidu.com -n 3")
    if result == 0:
        print("网络正常")
    else:
        print("网络故障")
    return result

if __name__ == '__main__':
    flag = 0
    #打开软件
    #open_stock_software()
    file_folder = '_'.join([str(i) for i in time.localtime(time.time())][:3])
    # 如果不存在当前文件夹则创建文件夹
    if not os.path.exists('D:/daytime_data/' + file_folder):
        os.mkdir('D:/daytime_data/' + file_folder)

    save_file_name = download_data_once(file_folder)

    get_ratio(save_file_name, file_folder)
    time.sleep(20)
    exit()

    # 获取当前时间
    cur_time = time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))
    while (int(cur_time.split('-')[0]) < 2021):
        hour, miniute, sec = time.localtime(time.time())[3:6]
        # 如果在9点以后没有打开软件则打开软件
        if hour >= 9 and hour < 15 and flag == 0:
            open_stock_software()
            print("open the software")
            flag = 1
        #收盘后关闭软件
        if flag == 1 and (hour > 15 or hour < 9):
            close_software()
            flag = 0
            print("software close!")
        file_folder = '_'.join([str(i) for i in time.localtime(time.time())][:3])
        # 如果不存在当前文件夹则创建文件夹
        if not os.path.exists('D:/daytime_data/' +file_folder):
            os.mkdir('D:/daytime_data/' +file_folder)
        if miniute % 20 == 0:
            # 保持网络畅通
            result = ping()
        # 从早上9:25开始收集数据，直到11；30
        if hour * 60 + miniute >= 550 and hour * 60 + miniute < 700 \
                and (int(time.strftime("%w")) >= 1 and int(time.strftime("%w")) <= 5):
            download_data_once(file_folder)
            time.sleep(10)
        # 继续收集下午数据（12:40 - 15:00）
        elif hour * 60 + miniute >= 760 and hour * 60 + miniute < 920 :
            download_data_once(file_folder)
            time.sleep(20)
        # 其余时间休息
        else:
            print("sleep for work")
            time.sleep(300)