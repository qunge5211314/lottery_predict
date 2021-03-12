#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-03-12
# Introduce: 大乐透数据清理
# Dependence
import pandas as pd


def clean_data():
    raw_data = pd.read_csv("../raw_data.csv", index_col="date")
    # 按日期从前到后排序
    cleaned_data = raw_data.sort_values("date")
    return cleaned_data


def save_cleaned_data(cleaned_data):
    cleaned_data.to_csv("../cleaned_data.csv")


if __name__ == '__main__':
    cleaned_data = clean_data()
    save_cleaned_data(cleaned_data)
