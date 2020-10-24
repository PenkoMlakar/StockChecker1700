# Script extracting data from yahoo finances

# Requirements:
# - pip3 install yfinance
# - pip3 install yahoo_fin
# - pip3 install requests_html
# - pip3 install django


def ExtractStocksData():

    import yfinance as yf1
    # import yahoo_fin.stock_info as yf2

    # stockSymbols = yf2.tickers_nasdaq() # Get all stocks (over 3000!)
    # print(f"Number of stocks: {len(stockSymbols)}")
    stockSymbols = ["AMD",
                    "INTC",
                    "NVDA",
                    "MX",
                    "NXPI",
                    "SOXX",
                    "TSLA",
                    "GOOG",
                    "SPOT",
                    "NOK",
                    "PYPL",
                    "ADSK",
                    "ADBE",
                    "ANSS",
                    "CSCO",
                    "DELL",
                    "QCOM",
                    "MSFT",
                    "WDC",
                    "TXN"]

    # stockSymbols = ["NFLX"]  # for testing

    # dummies
    data_12mo = [0]*len(stockSymbols)
    current = [0]*len(stockSymbols)

    i = 0
    for stock in stockSymbols:

        data_12mo[i] = yf1.download(stock, period="12mo")
        # keys: ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        # print(max(data_12mo[i]["High"]))

        # Get current price
        ticker_yahoo = yf1.Ticker(stock)
        data = ticker_yahoo.history()
        current_ = (data.tail(1)['Close'].iloc[0])
        print(f"Stock {stock}: current {current_}")

        current[i] = current_

        i += 1

    return stockSymbols, current, data_12mo


def filterStocks():

    import numpy as np
    import yfinance as yf1

    # Filter stocks
    stockSymbols, current, data_12mo = ExtractStocksData()

    filteredSymbols = []
    filteredPrevCloses = []
    filteredOpens = []
    filteredCurrents = []
    filteredOpenVsPrevClose = []
    filteredOpenVsCurrent = []
    for i in range(len(stockSymbols)):
        print("Stock: ", stockSymbols[i])
        print("Open: ", data_12mo[i]["Open"][-1])
        print("Close: ", data_12mo[i]["Close"][-2])
        premarket_up_percent = \
            (data_12mo[i]["Open"][-1]/data_12mo[i]["Close"][-2]-1)*100
        current_percent = (current[i]/data_12mo[i]["Close"][-2]-1)*100

        print("premarket_up_percent: ", premarket_up_percent)
        print("current_percent: ", current_percent)

        # SMA - SIMPLE MOVING AVERAGE
        pandas_table = yf1.download(stockSymbols[i], period="180m", interval="1m")
        # Calculating the n-window simple moving average
        sma = pandas_table.rolling(window=50).mean()
        print(f"Current: {current[i]}; SMA: {sma['Open'][-1]}")

        if (current_percent > premarket_up_percent) and \
           ((current_percent - premarket_up_percent) > 0.5) and \
           (sma["Open"][-1] < current[i]):
            filteredSymbols.append(stockSymbols[i])
            filteredPrevCloses.append(np.round(data_12mo[i]["Close"][-2], 2))
            filteredOpens.append(np.round(data_12mo[i]["Open"][-1], 2))
            filteredCurrents.append(np.round(current[i], 2))
            filteredOpenVsPrevClose.append(
                np.round((filteredOpens[-1]/filteredPrevCloses[-1]-1)*100, 2))
            filteredOpenVsCurrent.append(
                np.round((filteredCurrents[-1]/filteredPrevCloses[-1]-1)*100, 2))


        zipped = zip(filteredSymbols, filteredPrevCloses, filteredOpens,
                     filteredCurrents, filteredOpenVsPrevClose,
                     filteredOpenVsCurrent)

    return zipped


if __name__ == "__main__":
    # test
    # stockSymbols, current, data_12mo = ExtractStocksData()
    # print(stockSymbols)
    zipped = filterStocks()
    print(zipped)
