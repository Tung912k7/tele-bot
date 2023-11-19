from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext
import json 
import requests 

TOKEN = ('6828026388:AAGmDHwmtQz5K4NL9vM8YMRYOeZqS9vhsm8')
BOT_USERNAME= '@RyptCBot'

price = []
key = "https://api.binance.com/api/v3/ticker/price?symbol="
currencies = ['BTCUSDT']
url = key+currencies[0]
data = requests.get(url) 
data = data.json()
price.append(data['price'])


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a Coin Bot. What can I help you?')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Custom')

async def price_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(price)



#Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'Hi' or 'Hello' in processed:
        return 'Hello!'
    if 'How are you?' in processed:
        return 'Fine, thanks. And you?'
    if 'I' in processed:
        return 'Sorry, I do not understand you.'

    
    return 'I dont understand what you wrote...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}: "{type}"')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    print('Bot', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('price', price_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #errors
    app.add_error_handler(error)

    #polls the bot
    print('Polling......')
    app.run_polling(poll_interval=3)