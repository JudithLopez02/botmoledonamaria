import os
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# Estados para la conversación
SELECTING_ACTION, PLACING_ORDER, ASKING_QUESTION = range(3)

# Teclados personalizados
def main_keyboard():
    keyboard = [
        ['📦 Hacer pedido', '📖 Ver menú'],
        ['📍 Ubicación y horarios', '📞 Contacto'],
        ['❓ Preguntas frecuentes', '⭐ Special offer']
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def order_keyboard():
    keyboard = [
        ['🍯 Mole tradicional', '🌶️ Mole picante'],
        ['🐔 Mole con pollo', '🥩 Mole con carne'],
        ['🏠 Volver al menú principal']
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    welcome_text = f"""
¡Hola {user.first_name}! 👋🌶️

*Bienvenido a Mole Doña María* - ¡El auténtico sabor de México! 

¿En qué puedo ayudarte hoy? Selecciona una opción:
    """
    await update.message.reply_text(
        welcome_text,
        reply_markup=main_keyboard(),
        parse_mode='Markdown'
    )
    return SELECTING_ACTION

# Comando /menu
async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu_text = """
🍽️ *MENÚ MOLE DOÑA MARÍA* 🌶️

*MOLES TRADICIONALES:*
• 🍯 Mole Tradicional - $120
  (Suave y aromático, con chocolate y especias)

• 🌶️ Mole Picante - $140  
  (Para valientes, con chile habanero)

• 🌿 Mole Verde - $130
  (Con pipián y hierbas frescas)

*PLATILLOS ESPECIALES:*
• 🐔 Mole con Pollo - $180
  (1/4 de pollo + arroz + tortillas)

• 🥩 Mole con Carne de Res - $200
  (250g de carne + guarniciones)

• 🍖 Mole con Cerdo - $190
  (Costillas de cerdo glaseadas)

*EXTRAS:*
• 🍚 Arroz extra - $25
• 🫓 Tortillas (6 pzas) - $15
• 🥑 Guacamole - $40
• 🍹 Agua de horchata/jamaica - $30

*¡Todos incluyen arroz y tortillas!*
    """
    await update.message.reply_text(menu_text, parse_mode='Markdown')
    return SELECTING_ACTION

# Comando /ubicacion
async def show_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    location_text = """
📍 *UBICACIÓN Y HORARIOS*

🏠 *Dirección:*
Calle Sabores Mexicanos #123
Colonia Centro, Ciudad de México
📌 [Ver en Google Maps](https://maps.app.goo.gl/)

🕒 *Horarios:*
• Lunes a Viernes: 9:00 AM - 8:00 PM
• Sábados: 10:00 AM - 9:00 PM  
• Domingos: 11:00 AM - 6:00 PM

🚗 *Servicios:*
• ✅ Comer en local
• ✅ Para llevar
• ✅ Delivery (radio 5km)
    """
    await update.message.reply_text(location_text, parse_mode='Markdown')
    return SELECTING_ACTION

# Comando /contacto
async def show_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact_text = """
📞 *CONTACTO MOLE DOÑA MARÍA*

📱 *WhatsApp:* +52 1 55 1234 5678
📞 *Teléfono fijo:* (55) 1234 5678
📧 *Email:* mole.donamaria@hotmail.com

🌐 *Redes sociales:*
• 📷 Instagram: @MoleDoñaMaria
• 👍 Facebook: /MoleDoñaMariaOficial

💬 *¿Tienes dudas?* ¡Escríbenos! Respondemos en menos de 10 minutos.
    """
    await update.message.reply_text(contact_text, parse_mode='Markdown')
    return SELECTING_ACTION

# Comando /pedido
async def start_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    order_text = """
📦 *¡EMPEZCEMOS TU PEDIDO!*

Selecciona el tipo de mole que deseas:

• 🍯 Mole tradicional - $120
• 🌶️ Mole picante - $140
• 🐔 Mole con pollo - $180
• 🥩 Mole con carne - $200

*¡Todos incluyen arroz y tortillas!*
    """
    await update.message.reply_text(
        order_text, 
        reply_markup=order_keyboard(),
        parse_mode='Markdown'
    )
    return PLACING_ORDER

# Procesar pedido
async def process_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    order = update.message.text
    prices = {
        '🍯 Mole tradicional': 120,
        '🌶️ Mole picante': 140,
        '🐔 Mole con pollo': 180,
        '🥩 Mole con carne': 200
    }
    
    if order in prices:
        context.user_data['order'] = order
        context.user_data['price'] = prices[order]
        
        confirm_text = f"""
✅ *Pedido seleccionado:* {order}
💰 *Precio:* ${prices[order]} MXN

📝 *Para completar tu pedido:*
1. Envíanos un WhatsApp al +52 1 55 1234 5678
2. Menciona que viniste por Telegram
3. Recibirás 10% de descuento 🎉

*¡Gracias por preferir Mole Doña María!*
        """
        await update.message.reply_text(
            confirm_text,
            reply_markup=main_keyboard(),
            parse_mode='Markdown'
        )
        return SELECTING_ACTION
    elif order == '🏠 Volver al menú principal':
        await start(update, context)
        return SELECTING_ACTION
    else:
        await update.message.reply_text("Por favor selecciona una opción del menú:")
        return PLACING_ORDER

# Preguntas frecuentes
async def faqs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    faq_text = """
❓ *PREGUNTAS FRECUENTES*

*¿Hacen envíos a domicilio?*
✅ Sí, delivery en radio de 5km. Costo: $30 MXN

*¿Aceptan tarjetas?*  
✅ Sí, aceptamos todas las tarjetas de crédito/débito

*¿El mole es 100% natural?*
✅ Sí, usamos ingredientes frescos y naturales

*¿Tienen opciones vegetarianas?*
✅ Sí, nuestro mole tradicional es vegetariano

*¿Puedo pedir para eventos?*
✅ ¡Claro! Catering para eventos con 48h de anticipación

*¿Cuánto tiempo se conserva el mole?*
🕒 Hasta 5 días refrigerado, 3 meses congelado
    """
    await update.message.reply_text(faq_text, parse_mode='Markdown')
    return SELECTING_ACTION

# Special offer
async def special_offer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    offer_text = """
⭐ *¡OFERTA ESPECIAL!* ⭐

*Por tiempo limitado:*

🎉 *COMBO FAMILIAR* 🎉
• 1kg de mole + pollo/cerdo
• 1/2kg de arroz
• Tortillas (12 pzas)
• 1L de agua de sabor

💰 *Precio normal: $350*
💥 *¡PRECIO ESPECIAL: $299!*

*¡Solo menciona "TELEGRAM" y obtén este precio!*
    """
    await update.message.reply_text(offer_text, parse_mode='Markdown')
    return SELECTING_ACTION

# Manejar mensajes de texto
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == '📦 Hacer pedido':
        return await start_order(update, context)
    elif text == '📖 Ver menú':
        return await show_menu(update, context)
    elif text == '📍 Ubicación y horarios':
        return await show_location(update, context)
    elif text == '📞 Contacto':
        return await show_contact(update, context)
    elif text == '❓ Preguntas frecuentes':
        return await faqs(update, context)
    elif text == '⭐ Special offer':
        return await special_offer(update, context)
    else:
        await update.message.reply_text(
            "¡Hola! Selecciona una opción del menú:",
            reply_markup=main_keyboard()
        )
        return SELECTING_ACTION

# Comando /cancel
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '¡Operación cancelada! ¿En qué más puedo ayudarte?',
        reply_markup=main_keyboard()
    )
    return SELECTING_ACTION

# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")
    await update.message.reply_text(
        "¡Oops! Algo salió mal. Intenta de nuevo.",
        reply_markup=main_keyboard()
    )

# Función principal
def main():
    token = os.getenv("BOT_TOKEN")
    
    application = Application.builder().token(token).build()
    
    # Conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECTING_ACTION: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
            ],
            PLACING_ORDER: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, process_order)
            ]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    
    application.add_handler(conv_handler)
    application.add_error_handler(error)
    
    print("🤖 Bot Mole Doña María iniciado correctamente")
    application.run_polling()

if __name__ == '__main__':
    main()

