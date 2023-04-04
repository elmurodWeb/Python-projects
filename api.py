import requests
from telebot import TeleBot,types

TOKEN = '6044841261:AAHBrZ7PdzQk5isdtOPlqWFx6jGf9g6NNXg'
mybot = TeleBot(TOKEN)

# @mybot.message_handler(commands=['start'])
# def habar_yubor(message):
#     mybot.send_message(message.chat.id,"Salom men har kungi kurslar haqida ma'lumot beraman!")

@mybot.message_handler(commands=['start'])
def start(message):
    buttons = types.ReplyKeyboardMarkup(True)
    buttons.row("RUB","UZS","USD","EUR")
    # buttons.row()
    mybot.send_message(message.chat.id,"Salom men har kungi kurslar haqida ma'lumot beraman!",reply_markup=buttons)

@mybot.message_handler(func=lambda message:True)
def javob(message):
    kurs = message.text
    api_key = "244a5efb3de8a5341a58e307"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{kurs}"
    response = requests.get(url)
    data = response.json()
    javob = data["conversion_rates"]["UZS"]
    mybot.send_message(message.chat.id, javob)

mybot.polling()
