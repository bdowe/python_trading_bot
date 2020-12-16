import requests
from typing import List, Dict


class TDAPIClient():
    def __init__(self, client_id: str, redirect_uri: str, credentials_path: str) -> None:
        self.client_id: str = client_id
        self.redirect_uri: str = redirect_uri
        self.credentials_path: str = credentials_path
    
    def get_quote(self, symbol: str) -> dict:
        endpoint = f"https://api.tdameritrade.com/v1/marketdata/{symbol.upper()}/quotes"
        params = {"apikey": self.client_id}

        resp = requests.get(url=endpoint, params=params)
        return resp.json()

    def get_quotes(self, symbols: List[str]) -> List:
        endpoint = "https://api.tdameritrade.com/v1/marketdata/quotes"

        params = {
            "apikey": self.client_id,
            "symbol": ",".join(symbols).upper()
        }

        resp = requests.get(url=endpoint, params=params)
        return resp.json()

    def get_price_history(self, symbol: str, period_type: str ='year', period: int = 1, frequency_type: str = 'daily', frequency: int = 1, extended_hours: bool = True) -> List[Dict]:
        endpoint = f"https://api.tdameritrade.com/v1/marketdata/{symbol.upper()}/pricehistory"

        params = {
            "apikey": self.client_id,
            "period": str(period),
            "periodType": period_type,
            "frequency": str(frequency),
            "frequencyType": frequency_type,
            "needExtendedHoursData": extended_hours
        }

        resp = requests.get(url=endpoint, params=params)
        return resp.json()['candles']
    
    def get_price_histories(self, symbols: list, period_type: str ='year', period: int = 1, frequency_type: str = 'daily', frequency: int = 1, extended_hours: bool = True) -> List[Dict]:
        res = []

        for symbol in symbols:
            res += map(lambda d: {**d, "symbol": symbol}, self.get_price_history(symbol))

        return res

