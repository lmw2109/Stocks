import customtkinter as ctk

from settings import *
from nav import NavigationFrame
from info import InformationFrame
from data import DataHandler

class App(ctk.CTk):
    # setup
    def __init__(self):
        super().__init__()
        # config
        self._set_appearance_mode("system")
        # settings
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.resizable(False, False)
        self.title(TITLE)

        # data
        self.data = DataHandler()
        
        # create frames & widgets
        self.create(self.data)

    def create(self, data):
        NavigationFrame(parent = self,
                        data = data,
                        corner_radius = 0)
        InformationFrame(parent = self,
                         data = data,
                         corner_radius = 0)
        
# run
app = App()
app.mainloop()