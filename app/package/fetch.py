import yfinance as yf
import matplotlib.pyplot as plt
import io


def company_info(ticker):
    tick = yf.Ticker(ticker)
    return tick.info

def company_data(ticker):
    tick = yf.Ticker(ticker)
    history = tick.history(period = "max")
    return history

def plot_stats(ticker):
    tick = yf.Ticker(ticker)
    df = tick.history()
    return df['Close'].plot()
    