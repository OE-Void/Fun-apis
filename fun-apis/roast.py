import requests

class Roast:
    def __init__(self, url="https://insult.mattbas.org/api/insult"):
        self.url = url

    def get_punchline(self):
        line = requests.get(self.url)
        return line.text