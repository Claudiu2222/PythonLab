import tkinter as tk
from tkinter import ttk

class GuiApiClient(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("API Client")
        self.geometry("1000x600")
        self.resizable(False, False)
        self.initialize_gui()
        self.configure_styles()
    
    def initialize_gui(self):
        tab = ttk.Notebook(self)

        request_tab = RequestTab(tab)
        tab.add(request_tab, text="Request")

        tab.pack(expand=1, fill="both")

    def configure_styles(self):
        style = ttk.Style(self)
        style.theme_use('clam')

        style.configure('TNotebook', background='#2D2D2D', borderwidth=0)
        style.configure('TNotebook.Tab', background='#1a1a1a', foreground='white', lightcolor='#2D2D2D', darkcolor='#2D2D2D', borderwidth=0, padding=[20, 10])
        style.map('TNotebook.Tab', background=[('selected', '#2D2D2D')],focuscolor=[('focus', '')])

        style.map('TCombobox', fieldbackground=[('readonly', '#333333')])
        style.configure('TCombobox', background='#333333', foreground='white', borderwidth=0, fieldbackground='#333333') 
        self.option_add('*TCombobox*Listbox*Background', '#333333')
        self.option_add('*TCombobox*Listbox*Foreground', 'white')
        self.option_add('*TCombobox*Listbox*selectBackground', '#5FBA7D')
        self.option_add('*TCombobox*Listbox*selectForeground', 'white')
 
        style.configure('TFrame', background='#2D2D2D')

        # Style for buttons
        style.configure('TButton', background='#5FBA7D', foreground='white', font=('Helvetica', 10, 'bold'), borderwidth=0)
        style.map('TButton',
                  background=[('active', '#58a069'), ('pressed', '#50b369')],
                  foreground=[('pressed', '#FFFFFF'), ('active', '#FFFFFF')],
                  focuscolor=[('focus', '')])

        # Style for entries
        style.configure('TEntry', foreground='white', fieldbackground='#555555', borderwidth=0)



class RequestTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initialize_gui()
    
    def initialize_gui(self):
        self.create_widgets()
    
    def create_widgets(self):
        self.current_method_var = tk.StringVar()
        http_methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS']
        method_combobox =  ttk.Combobox(self, textvariable=self.current_method_var, values=http_methods, state='readonly', width=10)
        method_combobox.grid(row=0, column=0, padx=5, pady=20)
        method_combobox.current(0)


        self.url_entry = ttk.Entry(self, font=('Helvetica', 14), width=60)
        self.url_entry.grid(row=0, column=1, padx=5, pady=20)
        self.placeholder_text = "Enter your URL here"
        self.set_placeholder()

        send_button = ttk.Button(self, text="Send", command=self.send_request, style='TButton')
        send_button.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

        self.parameters_frame = ttk.LabelFrame(self, text='Parameters', padding=(20, 10))
        self.headers_frame = ttk.LabelFrame(self, text='Headers', padding=(20, 10))
        self.body_frame = ttk.LabelFrame(self, text='Body', padding=(20, 10))

    def set_placeholder(self):
        self.url_entry.insert(0, self.placeholder_text)
        self.url_entry.bind('<FocusIn>', self.clear_placeholder)
        self.url_entry.bind('<FocusOut>', self.add_placeholder)

    def clear_placeholder(self, event):
        if self.url_entry.get() == self.placeholder_text:
            self.url_entry.delete(0, tk.END)
    
    def add_placeholder(self, event):
        if self.url_entry.get() == '':
            self.url_entry.insert(0, self.placeholder_text)



    def send_request(self):
        url = self.url_entry.get()
        print("Sending request...")