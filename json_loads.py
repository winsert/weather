#!/usr/bin/env python
# -*- coding: UTF-8 -*-
##

__author__ = 'winsert@163.com'

import json
import demjson

filename = raw_input("请输入文件名(*.json):")

jf = open(filename, 'r')
#data = demjson.decode(jf)
data = json.loads(jf)

print data
print

for x, y in data.items():
    print x, y

jf.close()
