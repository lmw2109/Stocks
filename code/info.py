import customtkinter as ctk

'''
Contains all the components to build the
Information Panel.
'''

class InformationFrame(ctk.CTkFrame):
    def __init__(self, parent, data, **kwargs):
        super().__init__(parent, **kwargs)
        self.place(relx = 0.25, y = 0 , relwidth = 0.75, relheight = 1)