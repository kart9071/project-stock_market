#the link for all simplified ticker symbols

import yfinance as yf
import streamlit as st
import pandas as pd
import cufflinks as cf
import datetime

st.title("stock market app")
st.header("made for analysis of the thing")

st.markdown('''
a stock market trend analysis 
''')

st.write("------------------------------------")
st.sidebar.subheader('parameters')
st_date = st.sidebar.date_input("start date", datetime.date(2020, 1, 1))
en_date = st.sidebar.date_input("end date", datetime.date(2022, 1, 31))

tick_lst = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
ticksym = st.sidebar.selectbox('stock ticker', tick_lst)
tickdata = yf.Ticker(ticksym)
tickdf = tickdata.history(period = '1d', start = st_date, end = en_date)

str_logo = '<img src = %s' % tickdata.info['logo_url']
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