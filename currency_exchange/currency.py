import requests
from config_data import API_KEY


class Currency:
    def __init__(self):
        self.api_key = API_KEY
        self.url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/"

    def do_request(self, cur: str, exchange: str, amount: int = 1) -> dict | str:
        response = requests.get(self.url + cur + "/" + exchange + "/" + str(amount))
        if response.status_code == 200:
            return response.json()["conversion_result"]

