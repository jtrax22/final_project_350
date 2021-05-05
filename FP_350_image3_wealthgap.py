#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:25:24 2021

@author: jamestraxler
"""
from bs4 import BeautifulSoup as bs
import requests
import matplotlib.pyplot as plt
import pandas as pd
#from matplotlib import style
#import statsmodels.api as sm
import numpy as np
#from matplotlib import style
#from scipy import stats
#from sklearn.metrics import r2_score
#import json
#from pandas.io.json import json_normalize
#import matplotlib.pyplot as plt
#import math
from matplotlib.pyplot import figure

url = 'https://en.wikipedia.org/wiki/Wealth_inequality_in_the_United_States'

res = requests.get(url)
soup = bs(res.text, "html.parser")

wiki = pd.read_html(requests.get(url).text)
wealth = wiki[1]
hnw = wealth['Household Net Worth'].to_list()
top1 = wealth['Top 1%'].to_list()
names = wealth

q4 = wealth.iloc[0]
q4 = [(p) for p in q4]
q4 = q4[1:][:-1] #Quarter 4
integer_map = map(float, q4)
q4 = list(map(float, q4))


q2 = wealth.iloc[1]
q2 = [(p) for p in q2]
q2 = q2[1:][:-1] #Quarter 2
integer_map = map(float, q2)
q2 = list(map(float, q2))





names = [(col) for col in names.columns]
names = names[1:][:-1]
#print(names[0])
#graph
figure(num=None, figsize=(16, 6))
font = {'family' : 'Times New Roman',
        'weight' : 'bold',
        'size'   : 15}

plt.rc('font', **font)

plt.subplot(1, 2, 1)
plt.bar(names,q4, color='navy')
plt.yticks(np.arange(0, 50, 5))          
plt.xlabel('2016 Wealth status')
plt.ylabel('($ Trillions)')
plt.title("Household Networth")

plt.subplot(1, 2, 2)
plt.bar(names,q2, color = 'navy')
plt.yticks(np.arange(0, 50, 5))          
plt.xlabel('2020 Wealth status')
plt.ylabel('($ Trillions)')
plt.title("Household Networth")
plt.show()




