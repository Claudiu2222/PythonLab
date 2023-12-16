import requests


class ApiRequester:
    def __init__(self):
        pass

    def send_request(self, method, url, headers=None, body=None):
        try:
            response = requests.request(method, url, headers=headers, data=body)
            return {
                'status_code': response.status_code,
                'response_time': response.elapsed.total_seconds(),
                'content': response.text,
                'headers': dict(response.headers)
            }
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
