import requests
import json
from config import currencies, error_message, error_base, error_quote, error_amount, error_connection

class APIException(Exception):
    pass

class APIRequests:
    @staticmethod
    def get_price(message):
        try:
            message_split = message.text.split(' ')
            base, quote, amount = message_split
        except ValueError:
            raise APIException(error_message)
        else:
            try:
                if base.lower() not in currencies.keys() and base.upper() not in currencies.values():
                    raise APIException(error_base)
            except APIException:
                raise APIException(error_base)
            else:
                try:
                    if quote.lower() not in currencies.keys() and quote.upper() not in currencies.values():
                        raise APIException(error_quote)
                except APIException:
                    raise APIException(error_quote)
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
                            if len(base) == 3:
                                base_code = base.upper()
                            else:
                                base_code = currencies[base.lower()]
                            if len(quote) == 3:
                                quote_code = quote.upper()
                            else:
                                quote_code = currencies[quote.lower()]
                            request_result_1 = requests.get(f'https://min-api.cryptocompare.com/data/price?'
                                                            f'fsym={base_code}'
                                                            f'&tsyms={quote_code}')
                        except Exception:
                            raise APIException(error_connection)
                        else:
                            request_result_1_content = request_result_1.content
                            result_1 = json.loads(request_result_1_content)[quote_code]
                            result = round(result_1 * float(amount), 2)
                            result_message = f'{amount} {base_code} = {result} {quote_code}'

                            return result_message
