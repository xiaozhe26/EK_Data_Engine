# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 20:45:54 2020

@author: xiaozhe
"""


#导入pandas库
import pandas as pd
import os

#更改路径
os.chdir('D:/OneDrive/OneDrive - 上汽大众汽车有限公司/Date_Engine/Data_Engine_with_Python-master/Data_Engine_with_Python-master/L1/car_data_analyze')


#Step1 导入数据
data=pd.read_csv('car_complain.csv')
#print (data)

#Step2 数据预处理
data0 = data[['id','brand','car_model','problem']]
#print (data0)
data1 = data0['problem'].str.get_dummies(',')
data0 = data0.drop('problem',axis = 1).join(data1)
tags = data0.columns[3:]
#print(tags)

#Step3 按品牌
df = data0.groupby(['brand'])['id'].agg(['count'])
#print(df)
#统计不同类别数量
df1 = data0.groupby(['brand'])[tags].agg(['sum'])
#print(df1)
df2 = df.merge(df1, left_index=True, right_index=True, how='left')
df2.reset_index(inplace=True)
#print(df2)

#按总数降序排列
df2= df2.sort_values('count', ascending=False)
#print(df2)

#按抱怨种类排序
problem_nr = ('A11', 'sum')
print(df2.sort_values(problem_nr, ascending=False))


