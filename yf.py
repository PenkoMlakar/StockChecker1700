# Script extracting data from yahoo finances

# Requirements:
# - pip3 install yfinance
# - pip3 install django


def ExtractStocksData():

    import yfinance as yf

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
    # dummies
    data_1d = [0]*len(stockSymbols)
    data_7d = [0]*len(stockSymbols)
    data_30d = [0]*len(stockSymbols)
    data_12mo = [0]*len(stockSymbols)
    current = [0]*len(stockSymbols)

    i = 0
    for stock in stockSymbols:

        data_1d[i] = yf.download(stock, period="1d")
        data_7d[i] = yf.download(stock, period="7d")
        data_30d[i] = yf.download(stock, period="30d")
        data_12mo[i] = yf.download(stock, period="12mo")

        # keys: ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        print(max(data_12mo[i]["High"]))
        print(data_1d[i])

        # Get current price
        ticker_yahoo = yf.Ticker(stock)
        data = ticker_yahoo.history()
        current_ = (data.tail(1)['Close'].iloc[0])
        print(stock, current_)

        current[i] = current_

        i += 1

    return stockSymbols, current, data_1d, data_7d, data_30d, data_12mo


def filterStocks():
    # Filter stocks
    stockSymbols, current, data_1d, data_7d, data_30d, data_12mo = ExtractStocksData()

    filteredSymbols = []
    filteredPrevCloses = []
    filteredOpens = []
    filteredCurrents = []
    for i in range(len(stockSymbols)):
        print("Open: ", data_1d[i]["Open"][0])
        print("Close: ", data_1d[i]["Close"][0])
        premarket_up_percent = (data_1d[i]["Open"][0]/data_1d[i]["Close"][0]-1)*100
        current_percent = (current[i]/data_1d[i]["Close"][0]-1)*100

        print("premarket_up_percent: ", premarket_up_percent)
        print("current_percent: ", current_percent)

        if (current_percent > premarket_up_percent) and ((current_percent - premarket_up_percent) > 0.5):
            filteredSymbols.append(stockSymbols[i])
            filteredPrevCloses.append(data_1d[i]["Close"][0])
            filteredOpens.append(data_1d[i]["Open"][0])
            filteredCurrents.append(current[i])

        zipped = zip(filteredSymbols, filteredPrevCloses, filteredOpens,
                     filteredCurrents)

    return zipped


if __name__ == "__main__":
    # stockSymbols, current, data_1d, data_7d, data_30d, data_12mo = ExtractStocksData()
    # print(stockSymbols)
    zipped = filterStocks()
    print(zipped)
