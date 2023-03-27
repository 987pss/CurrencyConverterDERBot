# CurrencyConverterDERBot
Особенностями моего бота являются:
- возможность вводить названия валют на русском языке без учёта регистра;
- возможность вводить коды валют на английском языке без учёта регистра;
- возможность вводить количество исходной валюты в виде десятичной дроби с разделителем точка;
- текст сообщений для комманд /start и /help имеет различия;
- предусмотрены сообщения об ошибках ввода: неверный формат сообщения (количество передаваемых параметров не равно 3); ошибки в названии или коде исходной или конечной валют; ошибки в количестве исходной валюты (количество не соответсвует типу float или меньше 0);
- предусмотрено сообщение об ошибке подключения.

В файле config.py помимо токена также разместил словарь с валютами и тексты сообщений для бота.

@CurrencyConverterDERBot
https://t.me/CurrencyConverterDERBot
(удалён)
