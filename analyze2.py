#encoding=gbk
import pandas as pd
from snownlp import SnowNLP
from snownlp import sentiment
import matplotlib.pyplot as plt 


df=pd.read_csv('weibo_content.csv',usecols=[0,2])
#将dataframe转换为list
contents=df.values.tolist()
print(len(contents))
word=[]
score=[]

for content in contents:
	#print(content)
	try:
		a=[]
		s=SnowNLP(content[1])
		a.append(content[0])
		a.append(s.sentiments)
		score.append(a)
	except:
		print("something is wrong")
		a.append(content[0])
		a.append(0.5)
		score.append(a)
print(len(score))
data2 = pd.DataFrame(score)
data2.to_csv('id_scores2.csv', header=False, index=False, mode='a+')
