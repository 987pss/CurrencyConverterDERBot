import requests
import json
from config import currencies, error_message, error_currency_from, error_currency_to, error_amount, error_connection

class APIException(Exception):
    pass

class APIRequests:
    @staticmethod
    def get_price(message):
        try:
            message_split = message.text.split(' ')
            currency_from, currency_to, amount = message_split
        except ValueError:
            raise APIException(error_message)
        else:
            try:
                if currency_from.lower() not in currencies.keys() and currency_from.upper() not in currencies.values():
                    raise APIException(error_currency_from)
            except APIException:
                raise APIException(error_currency_from)
            else:
                try:
                    if currency_to.lower() not in currencies.keys() and currency_to.upper() not in currencies.values():
                        raise APIException(error_currency_to)
                except APIException:
                    raise APIException(error_currency_to)
                else:
                    try:
                        float(amount)
                        if float(amount) < 0:
                            raise APIException(error_amount)
                    except ValueError:
                        raise APIException(error_amount)
                    except APIException:
                        raise APIException(error_amount)
                    else:
                        try:
                            if len(currency_from) == 3:
                                currency_from_code = currency_from.upper()
                            else:
                                currency_from_code = currencies[currency_from.lower()]
                            if len(currency_to) == 3:
                                currency_to_code = currency_to.upper()
                            else:
                                currency_to_code = currencies[currency_to.lower()]
                            request_result_1 = requests.get(f'https://min-api.cryptocompare.com/data/price?'
                                                            f'fsym={currency_from_code}'
                                                            f'&tsyms={currency_to_code}')
                        except Exception:
                            raise APIException(error_connection)
                        else:
                            request_result_1_content = request_result_1.content
                            result_1 = json.loads(request_result_1_content)[currency_to_code]
                            result = round(result_1 * float(amount), 2)
                            result_message = f'{amount} {currency_from_code} = {result} {currency_to_code}'

                            return result_message
