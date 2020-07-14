# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 19:17:58 2020

@author: SOPHIE
"""
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from lxml import etree
from nltk.tokenize import word_tokenize

#导入数据
data = pd.read_csv('Market_Basket_Optimisation.csv',header=None)

trainsaction = []
for i in range(0,data.shape[0]):
    temp = []
    for j in range(0,data.shape[1]):
        item = str(data.values[i,j])
        if item!='nan':
            temp.append(item)
    trainsaction.append(temp)

# 生成词云
def create_word_cloud(f):
	print('根据词频，开始生成词云!')
	cut_text = word_tokenize(f)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	# 写词云图片
	wordcloud.to_file("wordcloud.jpg")
	# 显示词云文件
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()
    
all_word = ' '.join('%s' %item for item in trainsaction)
# 生成词云
create_word_cloud(all_word)
