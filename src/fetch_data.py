# fetch_data.py

import yfinance as yf
import pandas as pd

def download_price_data(tickers, start='2020-01-01', end='2023-01-01'):
    data = yf.download(tickers, start=start, end=end)['Adj Close']
    return data.dropna()

if __name__ == '__main__':
    tickers = ['MSFT', 'AAPL']
    df = download_price_data(tickers)
    df.to_csv('../data/sample_prices.csv')
