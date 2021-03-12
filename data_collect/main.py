#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-03-11
# Introduce: 大乐透数据收集
# Dependence
import requests
import json
import pandas as pd
import time

lottery_data_url = "https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry"
max_page = 10000000000000
columns = ["series", "date", "first", "second", "third", "fourth", "fifth", "sixth", "seventh"]


# 获取数据
def get_data():
    data = []
    for pageNo in range(1, max_page):
        time.sleep(2)
        res = requests.get(lottery_data_url, params={"gameNo": 85,
                                                     "provinceId": 0,
                                                     "pageSize": 30,
                                                     "isVerify": 1,
                                                     "pageNo": pageNo})
        json_data = json.loads(res.text)
        if not json_data.get("value").get("list"):
            break
        for info in json_data.get("value").get("list"):
            first, second, third, fourth, fifth, sixth, seventh = info.get("lotteryDrawResult").split(" ")
            data.append({"first": first,
                         "second": second,
                         "third": third,
                         "fourth": fourth,
                         "fifth": fifth,
                         "sixth": sixth,
                         "seventh": seventh,
                         "date": info.get("lotteryDrawTime")})
            # "draw_no": info.get("lotteryDrawNum")
    return data


# 保存数据
def save(data):
    date, draw_no, first, second, third, fourth, fifth, sixth, seventh = [], [], [], [], [], [], [], [], []
    for info in data:
        date.append(info.get("date"))
        # draw_no.append(info.get("draw_no"))
        first.append(info.get("first"))
        second.append(info.get("second"))
        third.append(info.get("third"))
        fourth.append(info.get("fourth"))
        fifth.append(info.get("fifth"))
        sixth.append(info.get("sixth"))
        seventh.append(info.get("seventh"))
    dic = {"date": date,
           # "draw_no": draw_no,
           "first": first,
           "second": second,
           "third": third,
           "fourth": fourth,
           "fifth": fifth,
           "sixth": sixth,
           "seventh": seventh}
    df = pd.DataFrame(dic)
    df.to_csv("../raw_data.csv")


if __name__ == '__main__':
    data = get_data()
    print(data)
    save(data)
