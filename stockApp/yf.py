# Script extracting data from yahoo finances

# Requirements:
# - pip3 install yfinance
# - pip3 install django

import yfinance as yf

stocks = ["AMD", "INTC", "NVDA"]

for stock in stocks:

    data_1d = yf.download(stock, period="1d")
    data_7d = yf.download(stock, period="7d")
    data_30d = yf.download(stock, period="30d")
    data_12mo = yf.download(stock, period="12mo")

    # keys: ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    print(max(data_12mo["High"]))
    print(data_1d)

    # Get current price
    ticker_yahoo = yf.Ticker(stock)
    data = ticker_yahoo.history()
    current = (data.tail(1)['Close'].iloc[0])
    print(stock, current)
