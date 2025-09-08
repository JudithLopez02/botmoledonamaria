import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('¡Hola! Soy tu bot funcionando correctamente ✅')

async def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("❌ ERROR: No se encontró BOT_TOKEN")
        print("⚠️  Asegúrate de configurar la variable en Railway")
        return
    
    print("✅ Token encontrado, iniciando bot...")
    
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    
    print("🤖 Bot iniciado correctamente")
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
