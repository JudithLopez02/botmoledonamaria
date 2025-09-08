from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

TOKEN = os.getenv("BOT_TOKEN")  # lo sacaremos de las variables de entorno en Railway

def start(update, context):
    update.message.reply_text("¡Hola! Soy tu bot y estoy activo 24/7 🚀")

def echo(update, context):
    update.message.reply_text(f"Dijiste: {update.message.text}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
