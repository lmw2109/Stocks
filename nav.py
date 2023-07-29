import customtkinter as ctk

from settings import *
from utils import read_list

'''
Contains all the components to build the
Navigation Panel.
'''

class NavigationFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.place(x = 0, y = 0 , relwidth = 0.25, relheight = 1)
        
        search_frame = SearchFrame(self,
                                   corner_radius = 0)
        search_frame.place(x = 0, y = 0, relwidth = 1, relheight = 0.07)
        
        scrollable_frame = ScrollableFrame(self,
                                           corner_radius = 0,
                                           label_text = "   My Stocks",
                                           label_text_color = 'gray',
                                           label_anchor = 'w')
        scrollable_frame.place(x = 0, rely = 0.07, relwidth =1, relheight = 0.86)
        
class SearchFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        search = ctk.CTkEntry(master = self,
                              placeholder_text = 'Search')
        search.pack(side = 'left', padx = 8, pady = 12, expand = True, fill = 'both')
        
class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        stocks = read_list("./user_stocks.json")
        
        for stock in stocks:
            stock_frame = StockFrame(self,
                                     symbol = stock
                                     )
            stock_frame.pack(padx = 12, pady = 6, expand = True, fill = 'x')

class StockFrame(ctk.CTkFrame):
    def __init__(self, parent, symbol, **kwargs):
        super().__init__(parent, **kwargs)
        symbol_label = ctk.CTkLabel(self, text = symbol)
        symbol_label.grid(row = 0, column = 0)
