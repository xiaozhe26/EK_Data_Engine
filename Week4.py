# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:48:40 2020

@author: SOPHIE
"""

#%%
import numpy as np
import pandas as pd
from efficient_apriori import apriori


data = pd.read_csv('Market_Basket_Optimisation.csv',header=None)

trainsaction = []
for i in range(0,data.shape[0]):
    temp = []
    for j in range(0,data.shape[1]):
        if str(data.values[i,j])!='nan':
            temp.append(str(data.values[i,j]))
    trainsaction.append(temp)

itemsets,rules = apriori(trainsaction,min_support=0.05, min_confidence=0.2)
print('频繁项集：', itemsets)
print('关联规则：', rules)

#%%
'''
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

data = pd.read_csv('Market_Basket_Optimisation.csv',header=None)

data['items'] = data[data.columns[0:]].apply(lambda x:'/'.join(x.dropna()),axis=1)
new_data = pd.DataFrame().append(data['items']).T
new_data_hot_encoded = data.drop('items',1).join(data.items.str.get_dummies('/'))#?报错“'function' object has no attribute 'str'”
print(new_data_hot_encoded.head())

# 挖掘频繁项集，最小支持度为0.05
itemsets = apriori(new_data_hot_encoded,use_colnames=True, min_support=0.05)
# 按照支持度从大到小进行时候粗
itemsets = itemsets.sort_values(by="support" , ascending=False) 
print('-'*20, '频繁项集', '-'*20)
print(itemsets)
# 根据频繁项集计算关联规则，设置最小提升度为2
rules =  association_rules(itemsets, metric='lift', min_threshold=2)
# 按照提升度从大到小进行排序
rules = rules.sort_values(by="lift" , ascending=False) 
#rules.to_csv('./rules.csv')
print('-'*20, '关联规则', '-'*20)
print(rules)

'''
