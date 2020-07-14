import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.ar_model import AutoReg
from sklearn import preprocessing
from keras.preprocessing.image import ImageDataGenerator

'''imported the data'''
sp = pd.read_csv('sp500.csv')
'''Am only interested in Adj Close, created new dataframe to adjust to this'''
dat = pd.DataFrame(data=sp['Date'])
dat['Adj Close'] = sp['Adj Close']
dat = dat.dropna()
dat['Date']=pd.to_datetime(dat['Date'])
# plt.plot(dat['Date'],dat['Adj Close'])
# plt.show()
# only un-comment above when u need it

'''Deep Learning cruise'''
# data has been viewed
# starting deep learning bullshit ride
# copy paste test and training shit from simple_forecasts.py

'''Feature Scaling'''
train_len = round(.8*len(dat))
# 1007
train, test = dat[1:train_len], dat[len(dat)-train_len:]
# date is creating a lot of problems so lets get rid of it entirely
dates=test['Date']              # for later
train=train['Adj Close']
test = test['Adj Close']
dat_scaled = preprocessing.scale(train)
'''
A very simple transformation is re-scaling the input between 0 and 1 , 
also known as MinMax scaling
could be very dumb, given our data
'''
# print(dat_scaled) --> [-1.0259653  -0.97292702 -0.96554803 ...  1.75520923  1.77668766 1.82021106]
# print(len(dat_scaled)) --> 1006

'''Supervised Learning algorithms'''
# fin until we build a few basic neural networks and get a hang of the sitch