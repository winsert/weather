# weather

用于从https://en.tutiempo.net/climate/01-2017/ws-548230.html爬取气象数据

济南的基本信息:
Data reported by the weather station: 548230 (ZSTN)
Latitude: 36.6 | Longitude: 116.98 | Altitude: 58

json_loads.py
用于从*.json提取数据，并恢复为字典

request.py      soup.txt
向指定网址发出request请求，并将结果保存到soup.txt

soup.py         soup.txt
用于对soup.txt进行步步分析

w.py    临时编程文件

year_month.py
实现按指定年份(最早到1957年)下载12个月的气象数据
