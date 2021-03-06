# Demo reads the csv file from pyfi1.py and plots OHLC candlestick chart with 50 & 200 day Moving Averages and Volumes

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')


df = pd.read_csv('aapl.csv', parse_dates=True, index_col=0)


df['200ma'] = df['Adj Close'].rolling(window=200).mean()

df['50ma'] = df['Adj Close'].rolling(window=50).mean()

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.xaxis_date()

ax1.plot(df.index, df['200ma'])
ax1.plot(df.index, df['50ma'])

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()


