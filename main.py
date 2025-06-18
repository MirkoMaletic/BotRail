
from flask import Flask, request
import os
from binance.client import Client
from telegram import Bot

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET = os.getenv("BINANCE_SECRET")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

client = Client(BINANCE_API_KEY, BINANCE_SECRET)
bot = Bot(token=TELEGRAM_TOKEN)

@app.route('/', methods=['GET'])
def home():
    return 'Bot je aktivan!'

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    if data:
        message = f"Webhook primljen: {data}"
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
