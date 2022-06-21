import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

ticker = yf.Ticker('IDEA.NS')
ticker.history()

#period = 'max'
#start = '2020-01-01'
#end = '2021-12-31'

df = ticker.history(start = '2020-01-01', end = '2021-12-31')

df['Close'].plot()
#plt.show()

#daily_return = (prev_close/current_close) -1
#log_daily_return = log(prev_close/current_close)

df['current_close'] = df['Close'].shift(1)
#print(df[['Close', 'current_close']])

df['daily_return'] = (df['Close']/df['current_close']) - 1
df['log_daily_return'] = np.log(df['Close']/df['current_close'])

df['daily_return'].plot()
#plt.show()

df['log_daily_return'].plot()
#plt.show()

df['daily_return'].hist(bins = 100)
#plt.show()

