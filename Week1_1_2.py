# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:09:27 2020

@author: xiaozhe
"""


#Action 1 求2+4+6+8+...+100的求和
sum = 0
number = 2
while number<101:
    sum = sum + number
    number = number + 2
print (sum)

#Action 2 统计全班的成绩 然后把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）
import pandas as pd
data = {'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data, index = ['张飞','关羽','刘备','典韦','许褚'])
print (df1)
print (df2)

chinese = df2['语文']
math = df2['数学']
english = df2['英语']
#平均分
print ("语文的平均分是：%s" %chinese.mean(axis = 0))
print ("数学的平均分是：%s" %math.mean(axis = 0))
print ("英语的平均分是：%s" %english.mean(axis = 0))
#最小成绩
print ("语文的最低分是：%s" %chinese.min(axis = 0))
print ("数学的最低分是：%s" %math.min(axis = 0))
print ("英语的最低分是：%s" %english.min(axis = 0))
#最大成绩
print ("语文的最高分是：%s" %chinese.max(axis = 0))
print ("数学的最高分是：%s" %math.max(axis = 0))
print ("英语的最高分是：%s" %english.max(axis = 0))
#方差
print ("语文的方差是：%s" %chinese.var(axis = 0))
print ("数学的方差是：%s" %math.var(axis = 0))
print ("英语的方差是：%s" %english.var(axis = 0))
#标准差
print ("语文的标准差是：%s" %chinese.std(axis = 0))
print ("数学的标准差是：%s" %math.std(axis = 0))
print ("英语的标准差是：%s" %english.std(axis = 0))
#总成绩排序输出
df2["总成绩"] = df2.apply(lambda x:x.sum(),axis =1)
print (df2)
df2.sort_values(by="总成绩",axis=0,ascending=False,inplace=True)
print(df2)
