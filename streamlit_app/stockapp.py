#the link for all simplified ticker symbols

from os import lstat
import yfinance as yf
import streamlit as st
import pandas as pd
import cufflinks as cf
import datetime
import numpy as np
from bs4 import BeautifulSoup
import requests
#from ta.volatility import BollingerBands
#from ta.trend import MACD
#from ta.momentum import RSIIndicator



st.title("stock market app")


st.markdown('''
a stock market trend analysis 
''')
#st.markdown('HELLO THIS IS SOMETHING TO DO IN THE MARKET WEBSITE')
st.write("------------------------------------")
st.sidebar.subheader('parameters')
st_date = st.sidebar.date_input("start date", datetime.date(2020, 1, 1))
en_date = st.sidebar.date_input("end date", datetime.date(2022, 1, 31))

tick_lst = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
ticksym = st.sidebar.selectbox('stock ticker', tick_lst)
tickdata = yf.Ticker(ticksym)
tickdf = tickdata.history(period = '1d', start = st_date, end = en_date)




url = "https://financialmodelingprep.com/financial-summary/" + ticksym
request = requests.get(url)

ticksym4 = st.sidebar.selectbox('choose the stock to compare with', tick_lst)
tickdata2 = yf.Ticker(ticksym4)
tickdf3 = tickdata2.history(period = '1d', start = st_date, end = en_date)

str_logo = '<img src = %s>' % tickdata.info['logo_url']
st.markdown(str_logo, unsafe_allow_html=True)

strname = tickdata.info['longName']
st.header('**%s**' % strname)

strsum = tickdata.info['longBusinessSummary']
st.info(strsum)

st.header('**ticker data**')
st.write(tickdf)

st.header('**bollinger bands**')
qf = cf.QuantFig(tickdf, title = 'figure', legend = 'top', name = 'gs')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure = True)
st.plotly_chart(fig)




if(st.sidebar.button("COMPARISON")):
    st.header(ticksym4)
    qf = cf.QuantFig(tickdf3, title = 'figure', legend = 'top', name = 'gs')
    qf.add_bollinger_bands()
    fig = qf.iplot(asFigure = True)
    st.plotly_chart(fig)
    
    
    
if(st.sidebar.button("stock analyser")):
    st.write(ticksym)
    stock = yf.Ticker(ticksym)
    tick_data4 = stock.history(period = '1d')
    prices = tick_data4['Close']
    volumes = tick_data4['Volume']
    
    #last_price = tick_data4['Last Price']

    lower = prices.min()
    upper = prices.max()
    st.write(prices)
    st.write(volumes)
    
    #st.write(stock.sustainability)
    st.write(stock.analysis)
    st.write(stock.actions)
    st.write(stock.cashflow)
    st.write(stock.major_holders)
    #st.write(stock.news)
    
    #st.write(last_price)

if(st.sidebar.button("action on the stock")):
    pass