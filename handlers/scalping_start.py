from telegram import Update
from telegram.ext import ContextTypes

async def scalping_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Scalping 1m/5m modul je aktiviran.")
