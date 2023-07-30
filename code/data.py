from yahooquery import Ticker
import os

from utils import read_list

'''
Initialises yahoo query using the user stock list.

- Stock history can be accessed after via DataHandler.tickers.history()
- Company data querys are not available at the moment, implementation delayed.
'''

class DataHandler():
    
    def __init__(self):
        # stocks
        self.symbols_list = read_list('./user_stocks.json')
        # data
        self.tickers = self._get_tickers()
            
    def _get_tickers(self) -> Ticker:
        try:
            stocks_request = " ".join(self.symbols_list)
            tickers = Ticker(stocks_request)
            print('Tickers accessed successfully.')
        except:
            print('Tickers could not be accessed.')
            return
        
        return tickers