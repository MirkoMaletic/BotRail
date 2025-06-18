from telegram import Update
from telegram.ext import ContextTypes

async def scs_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("SCS strategija 1h/4h je pokrenuta.")
