import requests
import json
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os
import sqlite3

#RVTLZQGNNKI1AZW7
#sgSC_ueaKrkbwOLrKud2LVF_JFovm6Eo

# Set the start and end date
start_date = '1990-01-01'
end_date = '2021-07-12'

tickers_list = ['AAPL', 'IBM', 'MSFT', 'WMT']

# Create placeholder for data
data = pd.DataFrame(columns=tickers_list)

tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
#fetching the data from the above loc
#print(tickers.head())


# Fetch the data in the array trackers list:
for ticker in tickers_list:
    data[ticker] = yf.download(ticker, start_date, end_date)['Adj Close']
'''   
# Print first 5 rows of the data
print(data)
'''
# Fetch the data
#the tickers['symbol'] are the tickers, so i need to pass them as the argument so how should i do it
    
data.plot(figsize=(10, 7))

# Show the legend
plt.legend()
# Define the label for the title of the figure
plt.title("Adjusted Close Price", fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()
