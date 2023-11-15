from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = ('6828026388:AAGmDHwmtQz5K4NL9vM8YMRYOeZqS9vhsm8')

async def start_command(updtae: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello!')

async def help_command(updtae: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a Coin Bot. What can I help you?')

async def custom_command(updtae: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Custom')

#Responses
def handle_response(text: str) -> str:
    if 'Hi' or 'Hello' in text:
        return 'Hello!'
    elif 'How are you?' in text:
        return 'Fine, thanks. And you?'
    else:
        return 'Sorry, I do not understand you.'