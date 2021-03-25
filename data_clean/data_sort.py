#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-03-12
# Introduce: 大乐透数据清理
# Dependence
import pandas as pd


def sort_data():
    raw_data = pd.read_csv("../raw_data.csv", index_col="date")
    # 按日期从前到后排序
    sorted_data = raw_data.sort_values("date")
    return sorted_data


def save_cleaned_data(sorted_data):
    sorted_data.to_csv("../sorted_data.csv")


if __name__ == '__main__':
    sorted_data = sort_data()
    save_cleaned_data(sorted_data)
