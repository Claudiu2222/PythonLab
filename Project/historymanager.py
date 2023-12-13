import json
import os

class HistoryManager:
    def __init__(self):
        self.filepath = os.path.join(os.getcwd(), 'history.json')
        

    def load_history(self):
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except Exception:
            return None

    def append_request(self, request_data):
        try:
            history_data = self.load_history()
            if history_data is None:
                history_data = []
            history_data.append(request_data)
            with open(self.filepath, 'w') as file:
                json.dump(history_data, file)
            return history_data
        except IOError:
            print("ERROR wriTing to file")
            return None
        
    def delete_history(self):
        try:
            with open(self.filepath, 'w') as file:
                json.dump([], file)
            return []
        except IOError:
            print("ERROR deleting the history")
            return None