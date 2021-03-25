#!python3
# -*- coding: utf-8 -*-
# Author: JustinHan
# Date: 2021-03-25
# Introduce: 数据one-hot处理
# Dependence
import numpy as np
import pandas as pd


def transfer_one_hot(data, max_value):
    one_hot_data = np.zeros((data.shape[0], max_value))
    for index, row in data.iterrows():
        for key, value in row.iteritems():
            one_hot_data[index, value - 1] = 1
    return one_hot_data


if __name__ == '__main__':
    data = pd.read_csv("../sorted_data.csv")
    red_ball_data = data.loc[:, ["first", "second", "third", "fourth", "fifth"]]
    blue_ball_data = data.loc[:, ["sixth", "seventh"]]
    red_ball_one_hot = transfer_one_hot(red_ball_data, max_value=35)
    blue_ball_one_hot = transfer_one_hot(blue_ball_data, max_value=12)
    red_ball_pd = pd.DataFrame(red_ball_one_hot)
    blue_ball_pd = pd.DataFrame(blue_ball_one_hot)
    red_ball_pd.to_csv("../red_ball_one_hot.csv")
    blue_ball_pd.to_csv("../blue_ball_one_hot.csv")
