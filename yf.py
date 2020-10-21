# Script extracting data from yahoo finances

# Requirements:
# - pip3 install yfinance
# - pip3 install django


def ExtractStocksData():

    import yfinance as yf

    stockLabels = ["AMD",
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
    data_1d = [0]*len(stockLabels)
    data_7d = [0]*len(stockLabels)
    data_30d = [0]*len(stockLabels)
    data_12mo = [0]*len(stockLabels)
    current = [0]*len(stockLabels)

    i = 0
    for stock in stockLabels:

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

    return stockLabels, current, data_1d, data_7d, data_30d, data_12mo


def filterStocks():
    # Filter stocks
    stockLabels, current, data_1d, data_7d, data_30d, data_12mo = ExtractStocksData()

    filteredStockLabels = []
    filteredCurrents = []
    filteredOpens = []
    for i in range(len(stockLabels)):
        print("Open: ", data_1d[i]["Open"][0])
        print("Close: ", data_1d[i]["Close"][0])
        premarket_increase_percent = (data_1d[i]["Open"][0]/data_1d[i]["Close"][0]-1)*100
        current_percentage = (current[i]/data_1d[i]["Close"][0]-1)*100

        print("premarket_increase_percent: ", premarket_increase_percent)
        print("current_percentage: ", current_percentage)

        if (current_percentage > premarket_increase_percent) and ((current_percentage - premarket_increase_percent) > 0.5):
            filteredStockLabels.append(stockLabels[i])
            filteredCurrents.append(current[i])
            filteredOpens.append(premarket_increase_percent)

        zipped = zip(filteredStockLabels, filteredCurrents, filteredOpens)

    return zipped


if __name__ == "__main__":
    # stockLabels, current, data_1d, data_7d, data_30d, data_12mo = ExtractStocksData()
    # print(stockLabels)
    zipped = filterStocks()
    print(filteredStockLabels)
