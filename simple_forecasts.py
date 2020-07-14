# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.ar_model import AutoReg

'''imported the data'''
sp = pd.read_csv('sp500.csv')
# print(sp.head())
# print(sp.columns)
'''Am only interested in Adj Close, created new dataframe to adjust to this'''
dat = pd.DataFrame(data=sp['Date'])
# dat = sp['Date']
dat['Adj Close'] = sp['Adj Close']
# print(dat.head())
''' fix any date issues (converting date from object to date obj)
also remove any NANs'''
dat = dat.dropna()
# print(dat.dtypes) ==> we see that date is an obj
dat['Date']=pd.to_datetime(dat['Date'])
# print(dat.dtypes) ==> now its a datetime64[ns] which is good
# plt.plot(dat['Date'],dat['Adj Close'])
# plt.show()
# only uncomment above when u need it
'''The graph shows a clear upward trend except for a massive downward turn
that downward turn was during covid. The data is taken from the last 5 yrs
there is a similar downward turn but not as severe in 2019
since the covid downward turn, its risen back to its original height p much
so in general, upward trend.
'''

'''going to split the data into train and test for modeling purposes
1. first find shape of data
print(dat.shape)
(1259, 2)
2. set up train and test, 80/20

'''
train_len = round(.8*len(dat))
# 1007
train, test = dat[1:train_len], dat[len(dat)-train_len:]
# date is creating a lot of problems so lets get rid of it entirely
dates=test['Date']
train=train['Adj Close']
test = test['Adj Close']
'''train the autoregression'''
model = AutoReg(train, lags=29)
# default lags
model_fit = model.fit()
# print('Coeffs: %s' % model_fit.params)

'''make predictions'''
preds = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
# there's a NAN value!!


print(len(preds), len(test))
# print(preds)
# for i in range(len(preds)):
#     print('predicted:%f, expected:%f' % (preds[i], test[i]))
#
'''Root mean squared error '''
mse = mean_squared_error(test, preds)
rmse = sqrt(mse)
print('Test RMSE: %.3f' % rmse)

'''plot results
in order to do this i have to set up the time series date 
'''
date_len = len(preds)+len(test)
# dates = pd.date_range(start='07/14/2015', end='07/13/2020')
pred_dates = pd.date_range(end='4/16/2023', periods=1007)
plt.plot(dates,test)
plt.plot(pred_dates,preds, color='red')
plt.show()

'''
The statsmodels API does not make it easy to update the model as new observations become available.

One way would be to re-train the AutoReg model each day as new observations become available, 
and that may be a valid approach, if not computationally expensive.
'''

# fin