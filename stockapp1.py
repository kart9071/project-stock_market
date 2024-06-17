import yfinance as yf
import streamlit as st
import pandas as pd
import cufflinks as cf
import datetime
import numpy as np
from bs4 import BeautifulSoup
import requests

tick_lst = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
option = st.sidebar.selectbox('Select one symbol', tick_lst)
import datetime
today = datetime.date.today()
before = today - datetime.timedelta(days=700)
start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('End date', today)

if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')