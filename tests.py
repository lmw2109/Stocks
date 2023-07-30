from utils import read_list
from yahooquery import Ticker
import datetime as dt

from data import DataHandler

data = DataHandler()

hist = data.tickers.history(start = dt.date(2023,1,1), end = dt.date(2023,6,30))

print(hist)