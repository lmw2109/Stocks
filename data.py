from yahooquery import Ticker
import pandas as pd

from utils import read_list

class DataHandler():
    
    def __init__(self):
        # stocks
        self.symbols_list = read_list("./user_stocks.json")
        # data
        self.tickers = self._get_tickers()
            
    def _get_tickers(self) -> Ticker:
        stocks_request = " ".join(self.symbols_list)
        try:
            tickers = Ticker(stocks_request)
            print('Tickers accessed successfully.')
        except:
            print('Tickers could not be accessed.')
            return
        
        return tickers