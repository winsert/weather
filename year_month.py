#!/usr/bin/env python
# -*- coding: UTF-8 -*-
## 程序模块化,将解析www.gushequ.com的结果title和href保存到gushequ.json

__author__ = 'winsert@163.com'

import requests, random, lxml, json

from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class weather():
    
    def __init__(self):

        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

    def getUrl(self, url): 
        UA = random.choice(self.user_agent_list) #随机选出一个user_agent
        headers = {'User-Agent': UA} #构造一个完整的user-agent
        try:
            response = requests.get(url, headers=headers)
            return response
        except Exception, e:
            print 'requests：',url, '时发生以下错误：'
            print e
            sys.exit()

    def getDict(self, url):

        content = self.getUrl(url)

        result = BeautifulSoup(content.text, 'lxml').find('div', class_="mt5 minoverflow").find_all('td')

        # 创建临时temp_list保存全部解析出的数据
        temp_list = []
        for h in result:
            temp_list.append(h.get_text())

        # 创建字典days_dict按日期保存整理后的数据
        days_dict = {}
        while len(temp_list) > 15: #舍弃最后一行数据(每列的平均数)
            day_key = temp_list.pop(0)
            #print day_key
            t_list = [] # 用临时表t_list保存从temp_list中截取的数据:共14项
            for i in range(14):
                t_list.append(temp_list.pop(0)) #从temp_list中截取数据追加到t_list中
            #print t_list
            days_dict[day_key] = tuple(t_list) #将t_list转换为元组，并追加到days_dict字典中

        print days_dict 


        # 验证days_dict字典中数据的准确性
        #for j in range(1, int(len(days_dict))+1):print j, days_dict[str(j)]

        return days_dict #将存有整个月份数据的字典返回

    def saveJson(self):
        yy = str(raw_input("请输入年份(最早至1957年):"))
        for m in range(1, 2): # 生成月份
            if m < 10:
                mm = '0'+str(m)
            else:
                mm = str(m)
            print "开始解析 %s-%s 月份的数据。" % (yy, mm)

            url = "https://en.tutiempo.net/climate/"+mm+"-"+yy+"/ws-548230.html"
            print "开始解析的页面：", url

            weather_dict = self.getDict(url)

            filename = yy+'_'+mm+'.json'
            print "正在保存:",filename
            wj = open(filename, 'w')
            wj.write(json.dumps(weather_dict))
            wj.close()

if __name__ == '__main__':
    
    weather_data = weather() #实例化
    weather_data.saveJson()
