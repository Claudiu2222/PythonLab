import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from httprequests import ApiRequester
from historymanager import HistoryManager
import urllib.parse
from urlmethods import encode_url, get_url_params,add_params_to_url
class GuiApiClient(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("API Client")
        self.geometry("1000x600")
        self.resizable(False, False)
        self.history_manager = HistoryManager()
        self.initialize_gui()
        self.configure_styles()
    
    def tab_change(self,event):
        if self.notebook.index('current') == 1:
            self.history_tab.load_history()
            
    def initialize_gui(self):
        self.notebook = ttk.Notebook(self)
        self.request_tab = RequestTab(self.notebook,self.history_manager)
        self.notebook.add(self.request_tab, text="Request")
        self.history_tab = HistoryTab(self.notebook, self.history_manager, self.request_tab)
        self.notebook.add(self.history_tab, text="History")
        self.notebook.bind('<<NotebookTabChanged>>', self.tab_change)
        self.notebook.pack(expand=1, fill="both")

    def configure_styles(self):
        style = ttk.Style(self)
        style.theme_use('clam')

        style.configure('TNotebook', background='#092635')
        style.configure('TNotebook.Tab', background='#1B4242', foreground='white')
        style.map('TNotebook.Tab', background=[('selected', '#092635')],focuscolor=[('focus', '')],padding=[('', [20, 5])])
        style.map('TCombobox', fieldbackground=[('', '#1B4242')])
        style.configure('TCombobox', background='#1B4242', foreground='white', borderwidth=0, fieldbackground='#1B4242') 
        self.option_add('*TCombobox*Listbox*Background', '#1B4242')
        self.option_add('*TCombobox*Listbox*Foreground', 'white')
        self.option_add('*TCombobox*Listbox*selectBackground', '#5C8374')
        self.option_add('*TCombobox*Listbox*selectForeground', 'white')
        style.configure('TFrame', background='#092635')
        style.configure('TButton', background='#5C8374', foreground='white', font=('Consolas', 10, 'bold'), borderwidth=0)
        style.map('TButton',
                  background=[('active', '#58a069'), ('pressed', '#50b369')],
                  foreground=[('pressed', '#FFFFFF'), ('active', '#FFFFFF')],
                  focuscolor=[('focus', '')])
        style.configure('TEntry', foreground='white', fieldbackground='#555555', borderwidth=0)

class RequestTab(ttk.Frame):
    def __init__(self, parent, history_manager):
        super().__init__(parent)
        self.parent = parent
        self.history_manager = history_manager
        self.initialize_gui()
        
    
    def initialize_gui(self):
        self.create_details_tab()
        self.create_widgets()
        self.create_response_tab()
        self.grid_columnconfigure(1, weight=1)
    
    def create_widgets(self):

        self.current_method_var = tk.StringVar()
        http_methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS']
        self.method_combobox =  ttk.Combobox(self, textvariable=self.current_method_var, values=http_methods, state='readonly', width=10,font=('Consolas', 12))
        self.method_combobox.grid(row=0, column=0, padx=5, pady=20)
        self.method_combobox.current(0)
        
        
        self.input_text = tk.StringVar()
        self.url_entry = ttk.Entry(self, font=('Consolas', 14), width=70,textvariable=self.input_text)
        self.url_entry.grid(row=0, column=1, padx=0, pady=20)
        self.input_text.trace_add('write', lambda x,y,z:self.extract_params_from_url())
        self.initialize_placeholder()
        
        send_button = ttk.Button(self, text="Send", command=self.send_request, style='TButton')
        send_button.grid(row=0, column=2, padx=5, pady=5)
        

    def initialize_placeholder(self):
        self.url_entry.insert(0, "Enter URL")
        self.url_entry.bind('<FocusIn>', self.set_focusin_placeholder)
        self.url_entry.bind('<FocusOut>', self.set_focusout_placeholder)

    def set_focusin_placeholder(self, event):
        if self.url_entry.get() == "Enter URL":
            self.url_entry.delete(0, tk.END)
    
    def set_focusout_placeholder(self, event):
        if self.url_entry.get() == '':
            self.url_entry.insert(0, "Enter URL")
        else:
            encoded_url = encode_url(self.input_text.get().rstrip(" "))
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, encoded_url)
    
    def extract_params_from_url(self):
        self.details_tab.populate_details({'params': get_url_params(self.url_entry.get())})
        
        

    def load_history_request(self, request):
        self.details_tab.populate_details(request)
        self.response_tab.set_response(request['content'], request['status'], request['response_time'])
        self.url_entry.delete(0, tk.END)
        self.url_entry.insert(0, request['url'])
        self.method_combobox.current(self.method_combobox['values'].index(request['method']))

    def send_request(self):
        url = self.url_entry.get().rstrip(" ")
        method = self.current_method_var.get()
        headers = self.details_tab.get_details()['headers']
        body = self.details_tab.get_details()['body']
        requester = ApiRequester()
        response = requester.send_request(method, url, headers, body)
        if response is None:
            return
        #print(response["headers"])
        request_to_save = { "method": method, "url": url, "status": response["status_code"], "response_time": response["response_time"], "content": response["content"], "headers": headers, "body": body}
        self.response_tab.set_response(response['content'], response['status_code'], response['response_time'])
        self.history_manager.append_request(request_to_save)

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
        self.parameters_frame = KeyValueEntry(self, "Parameter",is_param=True)
        self.headers_frame = KeyValueEntry(self, "Header")
        self.body_frame = ScrolledText(self.notebook, wrap=tk.WORD, font=('Consolas', 10), background="#092635", foreground="white")
        self.notebook.add(self.parameters_frame, text="Parameters")
        self.notebook.add(self.headers_frame, text="Headers")
        self.notebook.add(self.body_frame, text="Body")
    
    def get_details(self):
        return {
            'params': self.parameters_frame.get_key_value_pairs(),
            'headers': self.headers_frame.get_key_value_pairs(),
            'body': self.body_frame.get(1.0, tk.END)
        }
    def populate_details(self, request_data):
        self.parameters_frame.populate_entries(request_data.get('params', {}))
        self.headers_frame.populate_entries(request_data.get('headers', {}))
        self.body_frame.delete(1.0, tk.END)
        self.body_frame.insert(tk.END, request_data.get('body', ''))
    
    def update_url_params(self, params):
        url = self.parent.url_entry.get()
        self.parent.url_entry.delete(0, tk.END)
        self.parent.url_entry.insert(0, add_params_to_url(url, params))
        
    
class KeyValueEntry(ttk.Frame):
    def __init__(self, parent, title, is_param=False):
        super().__init__(parent)
        self.title = title
        self.parent =parent
        self.is_param = is_param
        self.key_value_pairs = []
        self.setup_widgets()

    def setup_widgets(self):
        self.listbox = tk.Listbox(self, height=5, selectmode="browser",background="#092635", foreground="white",font=('Consolas', 10))
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
        if self.is_param:
            self.parent.update_url_params(self.get_key_value_pairs())
    
    
    def populate_entries(self, entries):
        self.listbox.delete(0, tk.END)
        self.key_value_pairs = []
        for key, value in entries.items():
            self.key_value_pairs.append((key, value))
            self.listbox.insert(tk.END, f"{key}: {value}")
        

    def remove_selected_pair(self):
        selected_index = self.listbox.curselection()
        if len(selected_index) == 0:
            return
        self.key_value_pairs.pop(selected_index[0])
        self.listbox.delete(selected_index)
        if self.is_param:
           self.parent.update_url_params(self.get_key_value_pairs())
        
       
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
        response_label = ttk.Label(info_frame, text="Response", font=('Consolas', 10), foreground="white", background="#092635")
        response_label.grid(row=0, column=0, sticky='w')
        self.status_code_label = ttk.Label(info_frame, textvariable=self.status_var, font=('Consolas', 10), foreground="white", background="#092635")
        self.status_code_label.grid(row=0, column=1, sticky='e')
        self.time_taken_label = ttk.Label(info_frame, textvariable=self.time_var, font=('Consolas', 10), foreground="white", background="#092635")
        self.time_taken_label.grid(row=0, column=2, sticky='e')
        self.text_area = ScrolledText(self, wrap=tk.WORD, font=('Consolas', 10), background="#092635", foreground="white")
        self.text_area.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        self.text_area.config(state=tk.DISABLED) 
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

class HistoryTab(ttk.Frame):
    def __init__(self, parent, history_manager, request_tab):
        super().__init__(parent)
        self.parent = parent
        self.request_history = []
        self.history_manager = history_manager
        self.initialize_gui()
        self.request_tab = request_tab
        
    
    def initialize_gui(self):
        self.create_widgets()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
    def create_widgets(self):
        self.history_listbox = tk.Listbox(self, height=5, selectmode="browse", background="#092635", foreground="white", font=('Consolas', 10))
        self.history_listbox.pack(side="top", fill="both", expand=True)
        self.history_listbox.bind('<<ListboxSelect>>', self.on_select)
        self.remove_button = ttk.Button(self, text="Clear History", command=self.clear_history)
        self.remove_button.pack(side="bottom", pady=5)

    def load_history(self):
        self.request_history = self.history_manager.load_history()
        if self.request_history is None:
            self.request_history = []
        self.update_listbox()
    
    def update_listbox(self):
        self.history_listbox.delete(0, tk.END)
        for request in self.request_history:
            entry = f"{request['method']} {request['url']} - Status: {request['status']}"
            self.history_listbox.insert(tk.END, entry)
        
    def on_select(self, event):   
        index = self.history_listbox.curselection()
        if len(index) == 0:
            return
        selected_request = self.request_history[index[0]]
        self.request_tab.load_history_request(selected_request)
        self.parent.select(0)
        
    def clear_history(self):
        if self.history_manager.delete_history() is None:
            return
        self.request_history = []
        self.update_listbox()