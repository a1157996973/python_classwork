
#encoding=gbk

import urllib.request
import re
import pandas as pd
import numpy as np
import csv
import requests
import time


header = {'Content-Type':'application/json; charset=utf-8','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
Cookie = {'Cookie':'SINAGLOBAL=116548811372.39781.1617104195805; ULV=1623236241409:12:1:1:3514921946018.8765.1623236240420:1621234457944; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhqcJykAaPCSm3KlgqhAT6K5NHD95QNe02pSKMfe02RWs4Dqcj.i--fiKLhi-2Ri--Xi-zRiKyFi--fi-z7iKysi--Ni-i8i-is; ALF=1650979226; SCF=AsL88wugGT2KtOtaALDR4s1oWqHzsrKA5z9ujuUgoo-0n7g67wwL_pmcBgr5KHDiB3nnMhk2KhHHSdX9qxUjrGk.; UOR=,,www.baidu.com; _ga=GA1.2.1395989149.1618043219; __gads=ID=a5a0107a28b0c2fb-2209525e19c7008d:T=1618043221:S=ALNI_MbMKEF_QKuVSYxPm_bdU44XSV9r1g; SUB=_2A25Nw3q8DeRhGeFN6lMU9yvPyjSIHXVvTAb0rDV8PUJbkNAKLVrBkW1NQGYeKyLQ1YFwwl075Xq_rhjobIHT0UPz; SSOLoginState=1623657196; XSRF-TOKEN=wrFBktYhIBA5LAGDknJsDK_i; WBPSESS=lTPiWmhuFhmA28R4ScLsIa-3AkkXi00kTnUMqh0ePYEWiy7z33BumKI22abyy-Xu9wpYXfrMntZ44xwcyu5FVNyIXanXGBjbe6nx3BQE-gYU01dCRL2WzxJ-jSnpUnA6'}

weibo_comment_df=pd.read_csv('weibo_comment.csv',header=None,usecols=[1])
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
		data2.to_csv('weibo_user.csv', header=False, index=False, mode='a+')
	except:
		print("something is wrong")
		data1=[(weibo_comments[i][0],'没有','男','其他')]
		data2 = pd.DataFrame(data1)
		data2.to_csv('weibo_user.csv', header=False, index=False, mode='a+')
	time.sleep(0.25)

