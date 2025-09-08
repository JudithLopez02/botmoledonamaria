import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('¡Hola! Soy tu bot funcionando correctamente ✅')

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("❌ ERROR: No se encontró BOT_TOKEN")
        return
    
    print("✅ Token encontrado, iniciando bot...")
    
    # Crear la aplicación
    application = Application.builder().token(token).build()
    
    # Añadir handlers
    application.add_handler(CommandHandler("start", start))
    
    print("🤖 Bot iniciado correctamente")
    print("🚀 Iniciando polling...")
    
    # Iniciar el bot (FORMA CORRECTA)
    application.run_polling()

if __name__ == '__main__':
    main()
