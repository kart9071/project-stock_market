from os import lstat
import yfinance as yf
import streamlit as st
import pandas as pd
import cufflinks as cf
import datetime
import numpy as np
from bs4 import BeautifulSoup
import requests

def fetch_stock_data(st_date, en_date, ticksym):
    tickdata = yf.Ticker(ticksym)
    tickdf = tickdata.history(period='1d', start=st_date, end=en_date)
    return tickdf

def scrape_logo_url(company_name):
    url = f"https://www.google.com/search?q={company_name}+logo"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    logo_url = soup.find("img")["src"]
    return logo_url

def get_company_info(ticksym):
    tickdata = yf.Ticker(ticksym)
    company_name = tickdata.info.get('longName', '')
    print(company_name)
    if company_name:
        logo_url = scrape_logo_url(company_name)
        tickdata.info['logo_url'] = logo_url
        print(logo_url)
    return tickdata.info

def display_logo(company_info):
    str_logo = company_info.get('logo_url', '')
    if str_logo:
        str_logo = f'<img src="{str_logo}" width="200">'
    else:
        str_logo = 'No logo available'
    return str_logo

def main():
    st.title("Stock Market App")

    st.markdown('''
    A stock market trend analysis 
    ''')

    st.write("------------------------------------")
    st.sidebar.subheader('Parameters')
    st_date = st.sidebar.date_input("Start Date", datetime.date(2024,1,1))
    en_date = st.sidebar.date_input("End Date", datetime.date(2024, 4, 4))

    tick_lst = pd.read_csv('streamlit_app/textFile/tickerList.txt')
    ticksym = st.sidebar.selectbox('Stock Ticker', tick_lst)

    company_info = get_company_info(ticksym)

    str_logo = display_logo(company_info)
    # st.markdown(str_logo, unsafe_allow_html=True)

    strname = company_info['longName']
    st.header('**%s**' % strname)

    strsum = company_info['longBusinessSummary']
    st.info(strsum)

    tickdf = fetch_stock_data(st_date, en_date, ticksym)

    st.header('**Ticker Data**')
    st.write(tickdf)

    st.header('**Bollinger Bands**')
    qf = cf.QuantFig(tickdf, title='Figure', legend='top', name='gs')
    qf.add_bollinger_bands()
    fig = qf.iplot(asFigure=True)
    st.plotly_chart(fig)

    if st.sidebar.button("Comparison"):
        st.header("Comparison with another stock")
        # Add comparison functionality here

    if st.sidebar.button("Stock Analyzer"):
        st.header("Stock Analyzer")
        # Add stock analyzer functionality here

    if st.sidebar.button("Action on the Stock"):
        st.header("Action on the Stock")
        # Add action on the stock functionality here

if __name__ == "__main__":
    main()
