import os

import telebot

from utils import get_daily_horoscope
import json 
import requests

BOT_TOKEN = ('6828026388:AAGmDHwmtQz5K4NL9vM8YMRYOeZqS9vhsm8')

key = "https://api.binance.com/api/v3/ticker/price?symbol="


bot = telebot.TeleBot(BOT_TOKEN)
price = []
cry = []

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "I am a Coin Bot. What can I help you?")


@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    text = "What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)
'''
@bot.message_handler(commands=['price'])
def price_handler(message):
    text = "Name: "
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, crypto)

#@bot.message_handler(commands=['price'])
def crypto(message):
    price = []
    j = 0
    currencies = ['BTCUSDT', 'ETHUSDT','USDTUSDT']
    for i in currencies: 
	
        url = key+currencies[j] 
        data = requests.get(url) 
        data = data.json() 
        j = j+1
        price.append(data['price'])
    #bot.send_message(message.chat.id, price, parse_mode="Markdown")
'''
#@bot.message_handler(commands=['price'])
def get_crypto(message):
    j = 0
    currencies = ['BTCUSDT', 'ETHUSDT','USDTUSDT']
    for i in currencies:
        url = key+currencies[j] 
        data = requests.get(url) 
        data = data.json() 
        j = j+1
        price.append(data['price'])

@bot.message_handler(commands=['price'])
def crypto(message):
    '''
    btc = 'BTC: ' + price[0]
    eth = 'ETH: ' + price[1]
    usdt = 'USDT: ' + price[2]
    cry.append(btc)
    cry.append(eth)
    cry.append(usdt)
    '''
    bot.send_message(message.chat.id, (price[0],price[1], price[2]), parse_mode="Markdown")


def day_handler(message):
    sign = message.text
    text = "What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD."
    sent_msg = bot.send_message(
        message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_msg, fetch_horoscope, sign.capitalize())


def fetch_horoscope(message, sign):
    day = message.text
    horoscope = get_daily_horoscope(sign, day)
    data = horoscope["data"]
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\n*Sign:* {sign}\n*Day:* {data["date"]}'
    bot.send_message(message.chat.id, "Here's your horoscope!")
    bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()