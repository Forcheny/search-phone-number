"""
Version 0.000.002
2019-10-18  YONC
Added .upper() for comparing E164_number and phone_number, so that INITS can be searched.
Version 0.000.001
2019-10-14  YONC
"""

#-*- coding:utf-8 -*-

import csv
import os
import pandas as pd
from ConfigLoad import read_csv_path,read_search_column,read_display_column


def load_team_information(team):
    """
    Retrive the configuration from conf.ini through functions defined in ConfigLoad.py
    """
    csv_path = read_csv_path(team)
    search_columns = read_search_column(team)
    display_columns = read_display_column(team)
    return csv_path, search_columns, display_columns

def pandas_search(team,phone_number):
    """
    This method searches phone number for team in file 'csv_path'
    :param: team and phone number
    :return: destination rows, and the columns that are defined in conf.ini
    """

    file,search,display = load_team_information(team)
    if os.path.exists(file):
        data = []
        dest_head = []
        df = pd.read_csv(r'%s' % file, dtype='str', sep='|', low_memory=True)
        dest_head = get_column(display, df.columns)
        m = 5      #Max 5 rows are matched with the phone_number
        n = 0
        for target_column in search:
            df_mobile = df[target_column].values.tolist()
            i = 0
            for E164_number in df_mobile:
                if str(E164_number).replace(' ', '').upper() == phone_number.upper():
                    record = list(df.iloc[i, ])
                    data.append(record)
                    n += 1
                    i += 1
                    if n == m:
                        return data, dest_head
                else:
                    i += 1
            if n == m:
                return data, dest_head

        if data:
            return data, dest_head
        else:
            return [], []
    else:
        return 'The CSV path %s is not correct!' %file, []


def get_column(desthead, headrow):
    """
    Search the display column heads in headrow
    :return: the colmun's number in headrow, so that dispaly the required values in html
    """

    dest_column_numbers = []
    m = len(desthead)
    n = 0
    while n != m:
        i = 0
        for j in headrow:
            if j == desthead[n].replace('\'', ''):
                dest_column_numbers.append(i)
                continue
            else:
                i += 1
        n += 1
    return dest_column_numbers


# Test current method ,evaluate the method
# from time import time
# # t1 = time()
# s1,d1 = pandas_search('lsd','+4544448888')
# s2,d2 = pandas_search('pandoralsd','+85223208023')
# print(s1)
# print(d1)
# print(s2)
# print(d2)
# t2 = time()
# time = t2 - t1
# print(f'耗时： {time} 秒')
