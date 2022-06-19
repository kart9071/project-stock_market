import yfinance as yf

def company_info(ticker):
    tick = yf.Ticker(ticker)
    return tick.info

def company_data(ticker):
    tick = yf.Ticker(ticker)
    history = tick.history(period = "max")
    return history