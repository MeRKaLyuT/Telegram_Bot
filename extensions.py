import json
import requests
from Token import keys


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно рассчитать одинаковые валюты')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"""Не удалось обработать кол-во '{amount}'""")

        r = requests.get(f'https://v6.exchangerate-api.com/v6/0f7d02e333fc3568f1abfa80/latest/{keys[quote]}')
        data = json.loads(r.content)
        money = data['conversion_rates'][keys[base]] * float(amount)
        return money
