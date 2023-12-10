import tkinter as tk
from tkinter import ttk

class GuiApiClient(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("API Client")
        self.geometry("500x500")
        self.resizable(False, False)
