import inspect
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

msft = yf.Ticker('MSFT')
info = msft.info

# taking a dictionary input and turning it into a data frame.
# An error is thrown, so you have to use the orient index parameter to bypass this.
# Thereafter, you can transpose the df to orient it correctly.
msftdf = pd.DataFrame.from_dict(info, orient='index', )
msftdf = msftdf.transpose()
# print(msftdf.head())

# next we take a look at the history of a specific stock.
hist = msft.history(period='max', )
hist['Open'].plot(figsize=(300, 100))
plt.title('MSFT Opening Price History')
plt.ylabel('Price ($)')
plt.xlabel('Date')
plt.savefig(fname='MSFT Opening Price History.png')