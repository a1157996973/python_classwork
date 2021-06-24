import requests
import pandas as pd
import json
import time
import re

header = {'Content-Type':'application/json; charset=utf-8','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
Cookie = {'Cookie':'SCF=AsL88wugGT2KtOtaALDR4s1oWqHzsrKA5z9ujuUgoo-02gjtBO-aKgWkKy8nBrnzYe4aEnEkTkguIngmfQUHpZA.; SUB=_2A25Nw3q8DeRhGeFN6lMU9yvPyjSIHXVvTAb0rDV6PUJbktANLRXkkW1NQGYeKyjQosEDTVlLQtVdeiZj8yrNAZI8; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhqcJykAaPCSm3KlgqhAT6K5NHD95QNe02pSKMfe02RWs4Dqcj.i--fiKLhi-2Ri--Xi-zRiKyFi--fi-z7iKysi--Ni-i8i-is; XSRF-TOKEN=42aaca; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D231522type%253D1%2526t%253D10%2526q%253D%2523%25E9%2595%25BF%25E6%259C%259F%25E4%25B8%258D%25E4%25B8%258A%25E7%258F%25AD%25E4%25BC%259A%25E5%25AF%25BC%25E8%2587%25B4%25E4%25BB%2580%25E4%25B9%2588%25E5%2590%258E%25E6%259E%259C%2523%26oid%3D4647637804647685%26fid%3D231522type%253D1%2526t%253D10%2526q%253D%2523%25E9%2595%25BF%25E6%259C%259F%25E4%25B8%258D%25E4%25B8%258A%25E7%258F%25AD%25E4%25BC%259A%25E5%25AF%25BC%25E8%2587%25B4%25E4%25BB%2580%25E4%25B9%2588%25E5%2590%258E%25E6%259E%259C%2523%26uicode%3D10000011; _T_WM=16917732118'}

#评论翻页的关键字段
max_id = ""
#设置循环
while True:
	#评论第一页max_id为空值
	if max_id == "":
		url = "https://m.weibo.cn/comments/hotflow?id=4647637804647685&mid=4647637804647685&max_id_type=0"
	else:
		#显示max_id
		print(max_id)
		#评论后一页url中的max_id为前一页传递来的参数
		url = "https://m.weibo.cn/comments/hotflow?id=4647637804647685&mid=4647637804647685&max_id="+str(max_id)+"&max_id_type="+str(max_id_type) 
	print("请求的url是："+url)
	#request对象获取
	response = requests.get(url, headers=header, cookies=Cookie) 
	#json格式解析
	comment = response.json()
	print("requestion请求状态:"+str(comment['ok']))
	#如果Ok值为1，表示解析成功
	if comment['ok'] == 0:
		break
	#获取max_id值
	max_id = comment["data"]["max_id"]
	max_id_type = comment["data"]["max_id_type"]
	print("max_id is:"+str(max_id))
	print("max_id_type is:"+str(comment["data"]["max_id_type"]))
	#获取评论文本，并过滤符号和英文字符
	for comment_data in comment["data"]["data"]:
		data = comment_data["text"]
		p = re.compile(r'(<span.*>.*</span>)*(<a.*>.*</ a>)?')
		data = re.sub('[^\u4e00-\u9fa5]', '', data)
		data = p.sub(r'', data)
		data1=[(comment_data['created_at'],comment_data['user']['id'],comment_data['user']['screen_name'],data)]
		data2 = pd.DataFrame(data1)
		data2.to_csv('weibo_comment.csv', header=False, index=False, mode='a+')
		
	#休眠3秒，防止被系统认为是爬虫
	time.sleep(3)
