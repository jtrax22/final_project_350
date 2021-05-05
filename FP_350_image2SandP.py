#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:47:46 2021

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



plt.style.use('ggplot')

url = 'https://en.wikipedia.org/wiki/Household_income_in_the_United_States'


res = requests.get(url)
soup = bs(res.text, "html.parser")
#soup = bs(response.text, 'html.parser')



hhincome = pd.read_html(requests.get(url).text)
subframe = hhincome[3]
money = subframe['Mean household income'].to_list()
#ethnicity = subframe['Ethnic category'].to_list()
ethnicity = ['Asian','White','Hispanic/Latino','Black']

money = [e[1:] for e in money]
money = [(p) for p in money]

money = money[::-1]
money = [item.replace(",", "") for item in money]
integer_map = map(int, money)
money = list(map(int, money))


ethnicity = ethnicity[::-1]


#print(ethnicity)



fig = plt.figure()
ax = fig.add_axes([0,0,1,1])


plt.yticks(np.arange(0, 120000, 20000)) 

plt.xlabel('Ethnicity')
plt.ylabel('Income ($)')
plt.title("Average Household Income in March 2018")


plt.bar(ethnicity,money)




#print(hhincome)


#print(soup.find_all('a'))
