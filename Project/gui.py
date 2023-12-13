import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from httprequests import ApiRequester
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
        style.map('TNotebook.Tab', background=[('selected', '#2D2D2D')],focuscolor=[('focus', '')],padding=[('', [20, 5])])

        style.map('TCombobox', fieldbackground=[('readonly', '#333333')])
        style.configure('TCombobox', background='#333333', foreground='white', borderwidth=0, fieldbackground='#333333') 
        self.option_add('*TCombobox*Listbox*Background', '#333333')
        self.option_add('*TCombobox*Listbox*Foreground', 'white')
        self.option_add('*TCombobox*Listbox*selectBackground', '#5FBA7D')
        self.option_add('*TCombobox*Listbox*selectForeground', 'white')
 
        style.configure('TFrame', background='#2D2D2D')

        
        style.configure('TButton', background='#5FBA7D', foreground='white', font=('Helvetica', 10, 'bold'), borderwidth=0)
        style.map('TButton',
                  background=[('active', '#58a069'), ('pressed', '#50b369')],
                  foreground=[('pressed', '#FFFFFF'), ('active', '#FFFFFF')],
                  focuscolor=[('focus', '')])

        style.configure('TEntry', foreground='white', fieldbackground='#555555', borderwidth=0)



class RequestTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initialize_gui()
    
    def initialize_gui(self):
        self.create_widgets()
        self.create_details_tab()
        self.create_response_tab()
        self.grid_columnconfigure(1, weight=1)
    
    def create_widgets(self):

        self.current_method_var = tk.StringVar()
        http_methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS']
        method_combobox =  ttk.Combobox(self, textvariable=self.current_method_var, values=http_methods, state='readonly', width=10)
        method_combobox.grid(row=0, column=0, padx=5, pady=20)
        method_combobox.current(0)


        self.url_entry = ttk.Entry(self, font=('Helvetica', 14), width=70)
        self.url_entry.grid(row=0, column=1, padx=0, pady=20)
        self.placeholder_text = "Enter your URL here"
        self.set_placeholder()

        send_button = ttk.Button(self, text="Send", command=self.send_request, style='TButton')
        send_button.grid(row=0, column=2, padx=5, pady=5)
        

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
        method = self.current_method_var.get()
        params = self.details_tab.get_details()['params']
        headers = self.details_tab.get_details()['headers']
        body = self.details_tab.get_details()['body']
        requester = ApiRequester()
        response = requester.send_request(method, url, params, headers, body)
        if response is None:
            return
        print(response["headers"])
        self.response_tab.set_response(response['content'], response['status_code'], response['response_time'])

    def create_details_tab(self):
        self.details_tab = DetailsTab(self)
        self.details_tab.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')
        self.rowconfigure(1, weight=1)

    def create_response_tab(self):
        self.response_tab = ResponseTab(self)
        self.response_tab.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')
        self.rowconfigure(2, weight=0)


class DetailsTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)
        
        self.parameters_frame = KeyValueEntry(self.notebook, "Parameter")
        self.headers_frame = KeyValueEntry(self.notebook, "Header")
        self.body_frame = ScrolledText(self.notebook, wrap=tk.WORD, font=('Consolas', 10), background="#2D2D2D", foreground="white")

        self.notebook.add(self.parameters_frame, text="Parameters")
        self.notebook.add(self.headers_frame, text="Headers")
        self.notebook.add(self.body_frame, text="Body")
    
    def get_details(self):
        return {
            'params': self.parameters_frame.get_key_value_pairs(),
            'headers': self.headers_frame.get_key_value_pairs(),
            'body': self.body_frame.get(1.0, tk.END)
        }
    
class KeyValueEntry(ttk.Frame):
    def __init__(self, parent, title, **kwargs):
        super().__init__(parent, **kwargs)
        self.title = title
        self.key_value_pairs = []
        self.setup_widgets()

    def setup_widgets(self):
        self.listbox = tk.Listbox(self, height=5, selectmode="browser")
        self.listbox.pack(side="top", fill="both", expand=True)
        self.key_entry = ttk.Entry(self, width=20)
        self.key_entry.pack(side="left", padx=5, pady=5)
        self.value_entry = ttk.Entry(self, width=20)
        self.value_entry.pack(side="left", padx=5, pady=5)
        self.add_button = ttk.Button(self, text="Add", command=self.add_pair)
        self.add_button.pack(side="left", padx=5, pady=5)
        self.remove_button = ttk.Button(self, text="Remove", command=self.remove_selected_pair)
        self.remove_button.pack(side="left", padx=5, pady=5)

    def add_pair(self):
        key = self.key_entry.get()
        value = self.value_entry.get()
        if key and value:
            self.key_value_pairs.append((key, value))
            self.listbox.insert(tk.END, f"{key}: {value}")
            self.key_entry.delete(0, tk.END)
            self.value_entry.delete(0, tk.END)
        

    def remove_selected_pair(self):
        try:
            selected_index = self.listbox.curselection()
            self.listbox.delete(selected_index)
            #print(selected_index[0])
            if selected_index[0] > len(self.key_value_pairs):
                return
            self.key_value_pairs.pop(selected_index[0])
        except:
            pass
    def get_key_value_pairs(self):
        return dict(self.key_value_pairs)
    
class ResponseTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.config(height=250)
        self.create_widgets()
        
    def create_widgets(self):
        self.grid_propagate(False)

        self.status_var = tk.StringVar(value="")
        self.time_var = tk.StringVar(value="")

        info_frame = ttk.Frame(self, height=25, style='TFrame')
        info_frame.grid(row=0, column=0, sticky='ew', padx=5, pady=2)
        info_frame.grid_propagate(False)
        info_frame.columnconfigure(1, weight=1)

        response_label = ttk.Label(info_frame, text="Response", font=('Helvetica', 10), foreground="white", background="#2D2D2D")
        response_label.grid(row=0, column=0, sticky='w')

        self.status_code_label = ttk.Label(info_frame, textvariable=self.status_var, font=('Helvetica', 10), foreground="white", background="#2D2D2D")
        self.status_code_label.grid(row=0, column=1, sticky='e')

        self.time_taken_label = ttk.Label(info_frame, textvariable=self.time_var, font=('Helvetica', 10), foreground="white", background="#2D2D2D")
        self.time_taken_label.grid(row=0, column=2, sticky='e')

        self.text_area = ScrolledText(self, wrap=tk.WORD, font=('Consolas', 10), background="#2D2D2D", foreground="white")
        self.text_area.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        
        
    def set_response(self, response, status_code=None, time_taken=None):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)  
        self.text_area.insert(tk.END, response) 
        self.text_area.config(state=tk.DISABLED) 
        if status_code:
            self.status_var.set(f"Status: {status_code}")
        if time_taken:
            self.time_var.set(f"Time taken: {time_taken} seconds")
