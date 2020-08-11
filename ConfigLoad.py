"""
    Load the configuration from file,load the path of NN HR data,\
     and columns number for initial, position, mobile and manager
     Version 0.000.001--2019-10-10
        1.Move the configuration_file to local
        2.Create function for check section and read section
"""
# -*- coding: utf-8 -*-
import configparser
import os

configuration_file = r'C:/Apache24/Test_web/conf/conf.ini'


config = configparser.ConfigParser()
config.read(configuration_file)
config.sections()

def check_section(section):
    T = 0
    for s in config.sections():
        if s == section:
            T = 1
            break
        else:
            continue
    return T

def read_section(team):
    dict = []
    dict = config.items(team)
    return dict

def read_csv_path(team):
    dict = read_item_value(team,'csvfile')
    csv_path = os.path.normpath(dict[0])
    csv_file = dict[1]
    csv_path = os.path.join(csv_path, csv_file)
    return csv_path

def read_search_column(team):
    return read_item_value(team,'search')

def read_display_column(team):
    return read_item_value(team,'display')

def read_item_value(team,key):
    dict = []
    for k, v in config.items(team):
        # print(k)
        if key in str(k):
            # print(key)
            dict.append(v)
    return dict

# a = (read_config('C:\Apache24\Test_web\conf\conf.ini'))
# a = {}
# a = read_section('pandoralsd')
# print(check_section('pandora'))
# print(check_section('pandoralsd'))
# a = read_search_column('lsd')
# b = read_display_column('lsd')
# path1 = read_csv_path('lsd')
# path2 = read_csv_path('pandoralsd')
#
# print(a)
# print(b)
# print(path1)
# print(path2)

# print(a[0][1])

# dict(Config.items('Section')) --get all values from Sections
