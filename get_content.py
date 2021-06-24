
#encoding=gbk

import requests
import pandas as pd
import json
import time
import re 
import urllib
 

header = {'Content-Type':'application/json; charset=utf-8','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
Cookie = {'Cookie':'SCF=AsL88wugGT2KtOtaALDR4s1oWqHzsrKA5z9ujuUgoo-02gjtBO-aKgWkKy8nBrnzYe4aEnEkTkguIngmfQUHpZA.; SUB=_2A25Nw3q8DeRhGeFN6lMU9yvPyjSIHXVvTAb0rDV6PUJbktANLRXkkW1NQGYeKyjQosEDTVlLQtVdeiZj8yrNAZI8; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhqcJykAaPCSm3KlgqhAT6K5NHD95QNe02pSKMfe02RWs4Dqcj.i--fiKLhi-2Ri--Xi-zRiKyFi--fi-z7iKysi--Ni-i8i-is; WEIBOCN_FROM=1110006030; _T_WM=16917732118; XSRF-TOKEN=487b05; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D231522type%253D60%2526q%253D%2523%25E9%2595%25BF%25E6%259C%259F%25E4%25B8%258D%25E4%25B8%258A%25E7%258F%25AD%25E4%25BC%259A%25E5%25AF%25BC%25E8%2587%25B4%25E4%25BB%2580%25E4%25B9%2588%25E5%2590%258E%25E6%259E%259C%2523%2526t%253D10%26fid%3D231522type%253D1%2526t%253D10%2526q%253D%2523%25E9%2595%25BF%25E6%259C%259F%25E4%25B8%258D%25E4%25B8%258A%25E7%258F%25AD%25E4%25BC%259A%25E5%25AF%25BC%25E8%2587%25B4%25E4%25BB%2580%25E4%25B9%2588%25E5%2590%258E%25E6%259E%259C%2523%26uicode%3D10000011'}

url_base='https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D1%26t%3D10%26q%3D%23%E9%95%BF%E6%9C%9F%E4%B8%8D%E4%B8%8A%E7%8F%AD%E4%BC%9A%E5%AF%BC%E8%87%B4%E4%BB%80%E4%B9%88%E5%90%8E%E6%9E%9C%23&isnewpage=1&extparam=c_type%3D128%26pos%3D1-0-12%26unitid%3D26290&luicode=10000011&lfid=231648_-_4&page_type=searchall&page='

# 获取第1-50页搜索结果 
for ii in range(5000):

    url = url_base+str(ii)
    print(url)
    html = requests.get(url,headers=header,cookies=Cookie)
    b=html.json()
    try:
        for jj in range(len(html.json()['data']['cards'])):
            data1=[(html.json()['data']['cards'][jj]['mblog']['user']['id'],
            html.json()['data']['cards'][jj]['mblog']['user']['screen_name'],
            b['data']['cards'][jj]['mblog']['text'],
            html.json()['data']['cards'][jj]['mblog']['created_at'],
            html.json()['data']['cards'][jj]['mblog']['source'])]
            data2 = pd.DataFrame(data1)
            data2.to_csv('weibo_content.csv', header=False, index=False, encoding="utf-8-sig",mode='a+')
    except:
        print("抓取失败")
    print('page '+str(ii+1)+' has done')
    time.sleep(3)