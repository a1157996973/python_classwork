import pandas as pd


a=pd.read_csv('weibo_user2.csv',header=None,usecols=[0,2,3])
b=pd.read_csv('id_scores2.csv',header=None,usecols=[0,1])
weibo_sum_1=a.values.tolist()
weibo_sum_2=b.values.tolist()

sum_1={}
sum_2={}
sum=[]
#print(weibo_sum_2[0][])

for i in weibo_sum_1:
	
	x=i[2][0:3]
	
	if len(x)>2 and x[2]==' ':
		x=x[0:2]
	sum_1[i[0]]=[i[1],x]
for i in weibo_sum_2:
	sum_2[int(i[0])]=[i[1]]	

for i in sum_2:
	if i in sum_1:
		sum_1[i].append(sum_2[i][0])
for i in sum_1:
	if len(sum_1[i])<3:
		sum_1[i].append(0.5)
for i in sum_1:
	a=[i,sum_1[i][0],sum_1[i][1],sum_1[i][2]]
	sum.append(a)
	
data = pd.DataFrame(sum)
data.to_csv('weibo_sum2.csv',header=False, index=False,mode='a+')
print(1)
	
	