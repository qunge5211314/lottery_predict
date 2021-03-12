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
columns = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]


# 获取数据
def get_data():
    data = []
    for pageNo in range(1, max_page):
        time.sleep(0.5)
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
            data.append({"date": info.get("lotteryDrawTime"),
                         "first": first,
                         "second": second,
                         "third": third,
                         "fourth": fourth,
                         "fifth": fifth,
                         "sixth": sixth,
                         "seventh": seventh})
    return data


# 保存数据
def save(data):
    df = pd.DataFrame(data)
    df.set_index(["date"], inplace=True)
    df.to_csv("../raw_data.csv")


if __name__ == '__main__':
    data = get_data()
    save(data)
