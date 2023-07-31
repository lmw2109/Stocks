import customtkinter as ctk

from settings import *
from utils import read_list

'''
Contains all the components to build the
Navigation Panel.
'''

class NavigationFrame(ctk.CTkFrame):
    def __init__(self, parent, data, **kwargs):
        # frame setup
        super().__init__(parent, **kwargs)
        self.place(x = 0, y = 0 , relwidth = 0.25, relheight = 1)
        # data
        self.data = data
        # create
        self.create()
        
    def create(self):
        search_frame = SearchFrame(self,
                                   corner_radius = 0)
        search_frame.place(x = 0, y = 0, relwidth = 1, relheight = 0.12)
        
        scrollable_frame = ScrollableFrame(self,
                                           corner_radius = 0,
                                           label_text = "   My Stocks",
                                           label_text_color = 'gray',
                                           label_anchor = 'w')
        scrollable_frame.place(x = 0, rely = 0.12, relwidth = 1, relheight = 0.82)
        
        bottom_frame = BottomFrame(self,
                                   corner_radius = 0)
        bottom_frame.place(x = 0, rely = 0.94, relwidth = 1, relheight = 0.06)
        
class SearchFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        search = ctk.CTkEntry(master = self,
                              height = 32,
                              placeholder_text = 'Search')
        search.pack(side = 'left', padx = 12, pady = 12, expand = True, fill = 'x')
        
class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        stocks = read_list("./user_stocks.json")
        
        for stock in stocks:
            stock_frame = StockFrame(self,
                                     symbol = stock
                                     )
            stock_frame.pack(padx = 12, pady = 4, expand = True, fill = 'both')

class StockFrame(ctk.CTkFrame):
    def __init__(self, parent, symbol, **kwargs):
        super().__init__(parent, **kwargs)
        symbol_label = ctk.CTkLabel(self, text = symbol)
        symbol_label.pack()
        price_label = ctk.CTkLabel(self, text = '')
        price_label.pack()
        
class BottomFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        bottom_label = ctk.CTkLabel(self, 
                                    text = 'yahoo!finance',
                                    text_color = 'gray')
        bottom_label.pack(side='left', padx = 12)
