import telebot
from config import TOKEN, currencies, user_guide_start, user_guide_help
from extensions import APIRequests

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_user_guide(message):
    user_first_name = message.from_user.first_name
    user_guide_message = f'{user_first_name},\n\n{user_guide_start}'
    bot.send_message(message.chat.id, user_guide_message)

@bot.message_handler(commands=['help'])
def send_user_guide(message):
    user_guide_message = f'{user_guide_help}'
    bot.send_message(message.chat.id, user_guide_message)

@bot.message_handler(commands=['values'])
def send_available_currencies(message):
    available_currencies_message = 'Доступные валюты:\n'
    for key in currencies:
        available_currencies_message += f'\n{key} ({currencies[key]})'
    bot.send_message(message.chat.id, available_currencies_message)

@bot.message_handler(content_types=['text'])
def send_result(message):
    try:
        result_message = APIRequests.get_price(message)
    except Exception as error:
        bot.send_message(message.chat.id, error)
    else:
        bot.send_message(message.chat.id, result_message)

bot.polling(none_stop=True)