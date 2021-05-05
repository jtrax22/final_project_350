#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 15:14:35 2021

@author: jamestraxler
"""
from bs4 import BeautifulSoup as bs
import requests
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
#import statsmodels.api as sm
import numpy as np
#from matplotlib import style
#from scipy import stats
#from sklearn.metrics import r2_score

url = 'https://finance.yahoo.com/quote/%5EGSPC/history?period1=-1325635200&period2=1619395200&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true'

response = requests.get(url)
soup = bs(response.text, 'html.parser')
prices = pd.read_html(url, attrs = {'data-test':'historical-prices'})
subframe = prices[0].iloc[:,[0,5]]

#subframe.plot(kind = 'scatter', x = 0, y = 1)

#dates = subframe['Date'].to_list()[:-1]
#print(dates)

prices = subframe['Adj Close**'].to_list()[:-1]


prices = [float(p) for p in (prices)]
prices = [int(p) for p in prices]
prices = prices[::-1]


#print(prices)
months = [i for i in range(len(prices))]
#print(months)
#stats


'''
#linear regression

#res = stats.linregress(months, prices)

#r2score = r2_score(months, prices)

rsquared = f"R-squared: {res.rvalue**2:.6f}"
plt.plot(months, prices, 'o', label='original data')
plt.plot(months, res.intercept + res.slope*months, 'r', label='fitted line')
plt.legend()
plt.show()








plt.plot(months, prices, 'o', label='original data')
plt.plot(months, res.intercept + res.slope*months, 'r', label='regression line')

'''
#customize
plt.scatter(x = months, y = prices) #add from month
plt.xlabel('Months (starting from Jan 01, 2013 to April 01, 2021')
plt.ylabel('adjusted closing price ($)')
plt.title("S&P 500")
#plt.annotate("March 2018", (60,2600))
plt.annotate('March 2018', xy=(60, 2600), xytext=(20, 3000),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

x = np.array(months)
y = np.array(prices)
plt.plot(x, y, 'o')
m, b = np.polyfit(months, prices, 1)
plt.plot(x, m*x + b)

#plt.show()



'''




print("R-squared: %f" % r_value**2)
slope, intercept, r_value, p_value, std_err = stats.linregress(x=months,prices)  
print("R: %f" % r_value)
slope, intercept, r_value, p_value, std_err = stats.linregress(x=months,prices)  
print("P: %f" % p_value)
'''

