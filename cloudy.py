import pandas as pd
import matplotlib.pyplot as plt
import jieba
import wordcloud

df=pd.read_csv('weibo_comment.csv',usecols=[3])

text = df.values.tolist()

cut_text = jieba.lcut(str(text),cut_all=Ture)

result = " ".join(cut_text)

wc = wordcloud.WordCloud(
    font_path='simhei.ttf',     
    background_color='white',
    width=1000,
    height=600,
    max_font_size=50,            
    min_font_size=10,
    max_words=1000
)
wc.generate(result)
wc.to_file('tuend.png')    

plt.figure('tuend')   
plt.imshow(wc)
plt.axis('off')     
plt.show()
