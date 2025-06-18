
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from handlers.start import start_command
from handlers.status import status_command

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Nepoznata komanda. Koristi /start ili /status.")

def main():
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    if not telegram_token:
        raise Exception("TELEGRAM_TOKEN nije postavljen.")

    app = ApplicationBuilder().token(telegram_token).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("status", status_command))
    app.add_handler(CommandHandler(None, unknown_command))

    print("Bot je pokrenut...")
    app.run_polling()

if __name__ == "__main__":
    main()
