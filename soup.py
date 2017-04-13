#!/usr/bin/env python
# -*- coding: UTF-8 -*-
## 对soup.txt进行步步解析

import requests
from bs4 import BeautifulSoup
import os
 
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sp = open('./soup.txt', 'r')

result = BeautifulSoup(sp.read(), 'lxml').find('div', class_="mt5 minoverflow").find_all('td')

# 创建临时temp_list保存全部解析出的数据
temp_list = []
for h in result:
    temp_list.append(h.get_text())

# 创建字典days_dict按日期保存整理后的数据
days_dict = {}
while len(temp_list) > 15: #舍弃最后一行数据(每列的平均数)
    day_key = temp_list.pop(0)
    #print day_key
    t_list = [] # 用临时表t_list保存从temp_list中截取的数据
    for i in range(14):
        t_list.append(temp_list.pop(0)) #从temp_list中截取数据追加到t_list中
    #print t_list
    days_dict[day_key] = tuple(t_list) #将t_list转换为元组，并追加到days_dict字典中
#print days_dict 

# 验证days_dict字典中数据的准确性
for j in range(1, int(len(days_dict))+1):
    print j, days_dict[str(j)]

sp.close() # 关闭文件
