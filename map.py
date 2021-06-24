import pandas as pd
from snownlp import SnowNLP
from snownlp import sentiment
import matplotlib.pyplot as plt 
from pyecharts.charts import Map
from pyecharts.faker import Faker
from pyecharts import options as opts


#读取csv文件

df=pd.read_csv('weibo_sum.csv')
map_2=df.values.tolist()
arr={'河北':[0,0]}
end=[]

print(map_2)

for i in map_2:
	if i[2] in arr:
		arr[i[2]][0]+=i[3]
		arr[i[2]][1]+=1
	else:
		arr[i[2]]=[i[3],1]
for i in arr:
	a=[i,arr[i][0]/arr[i][1]*10]
	end.append(a)


# 连续性数据显示，不同颜色不同省份
def map_visualmap() -> Map:
    c = (
        Map()
        .add("", end, "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="连续型数据"),
            visualmap_opts=opts.VisualMapOpts(max_= 10),
        )
    )
    return c
if __name__ == '__main__':
    city_ = map_visualmap()
    city_.render(path="test_map_0.html")


























