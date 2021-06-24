
#encoding=gbk

import urllib.request
import re
import pandas as pd
import numpy as np
import csv
import requests
import time


header = {'Content-Type':'application/json; charset=utf-8','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
Cookie = {'Cookie':'SCF=AsL88wugGT2KtOtaALDR4s1oWqHzsrKA5z9ujuUgoo-02gjtBO-aKgWkKy8nBrnzYe4aEnEkTkguIngmfQUHpZA.; SUB=_2A25Nw3q8DeRhGeFN6lMU9yvPyjSIHXVvTAb0rDV6PUJbktANLRXkkW1NQGYeKyjQosEDTVlLQtVdeiZj8yrNAZI8; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhqcJykAaPCSm3KlgqhAT6K5NHD95QNe02pSKMfe02RWs4Dqcj.i--fiKLhi-2Ri--Xi-zRiKyFi--fi-z7iKysi--Ni-i8i-is; _T_WM=91908511801; SSOLoginState=1623657196; WEIBOCN_FROM=1110006030; XSRF-TOKEN=2502dc; MLOGIN=1; M_WEIBOCN_PARAMS=uicode%3D20000061%26fid%3D4647637804647685%26oid%3D4647637804647685'}

weibo_comment_df=pd.read_csv('weibo_content.csv',header=None,usecols=[0])
weibo_comments=weibo_comment_df.values.tolist()
print(len(weibo_comments))
for i in range(len(weibo_comments)):
	#print(type(weibo_comment[0]))
	url_base_1="http://weibo.cn/"
	url_base_2="/info"
	url=url_base_1+str(weibo_comments[i][0])+url_base_2
	print(i)
	print(url)
	try:
		html = requests.get(url,headers=header,cookies=Cookie)
		nickname=re.findall(r'<div class="c">昵称:(.*?)<br/>',html.text)
		print(nickname)
		sex=re.findall(r'<br/>性别:(.*?)<br/>',html.text)
		print(sex)
		location=re.findall(r'<br/>地区:(.*?)<br/>',html.text)
		print(location)
		data1=[(weibo_comments[i][0],nickname[0],sex[0],location[0])]
		data2 = pd.DataFrame(data1)
		data2.to_csv('weibo_user2.csv', header=False, index=False, mode='a+')
	except:
		print("something is wrong")
		data1=[(weibo_comments[i][0],'没有','男','其他')]
		data2 = pd.DataFrame(data1)
		data2.to_csv('weibo_user2.csv', header=False, index=False, mode='a+')
	time.sleep(1)

