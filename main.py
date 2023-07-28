import tkinter as tk
import customtkinter as ctk

from settings import *

class App(ctk.CTk):
    # setup
    def __init__(self):
        super().__init__()
        # config
        self._set_appearance_mode("System")
        # settings
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.title(TITLE)
    
# run
app = App()
app.mainloop()
