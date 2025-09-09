import os
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# Estados para la conversación
SELECTING_ACTION, PLACING_ORDER, ASKING_QUESTION, SURVEY, RECOMMENDATIONS = range(5)

# Teclados personalizados
def main_keyboard():
    keyboard = [
        ['📦 Hacer pedido', '📖 Ver menú'],
        ['📍 Puntos de venta', '🕒 Horarios de atención'],
        ['ℹ️ Información del producto', '⭐ Novedades'],
        ['❓ Preguntas frecuentes', '📊 Encuestas'],
        ['💡 Recomendaciones', '🍳 Recetas'],
        ['👋 Despedida']
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def order_keyboard():
    keyboard = [
        ['🍯 Mole tradicional', '🌶️ Mole picante'],
        ['🐔 Mole con pollo', '🥩 Mole con carne'],
        ['🏠 Volver al menú principal']
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def survey_keyboard():
    keyboard = [
        ['⭐ 5 Estrellas', '⭐⭐⭐ 3 Estrellas'],
        ['⭐⭐⭐⭐ 4 Estrellas', '⭐⭐ 2 Estrellas'],
        ['⭐ 1 Estrella', '🏠 Volver al menú principal']
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Comando /start - Bienvenida (se mantiene igual)
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

# Horarios de atención
async def show_hours(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hours_text = """
🕒 *HORARIOS DE ATENCIÓN*

🏪 *Tienda Principal:*
• Lunes a Viernes: 9:00 AM - 8:00 PM
• Sábados: 10:00 AM - 9:00 PM  
• Domingos: 11:00 AM - 6:00 PM

🚚 *Servicio a Domicilio:*
• Lunes a Domingo: 10:00 AM - 7:00 PM

📞 *Atención Telefónica:*
• Lunes a Domingo: 8:00 AM - 9:00 PM

*¡Estamos para servirte!* 😊
    """
    await update.message.reply_text(hours_text, parse_mode='Markdown')
    return SELECTING_ACTION

# Preguntas frecuentes (actualizada)
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

*¿Hacen envíos a otros estados?*
✅ Sí, a toda la República Mexicana
    """
    await update.message.reply_text(faq_text, parse_mode='Markdown')
    return SELECTING_ACTION

# Mensaje de despedida
async def goodbye(update: Update, context: ContextTypes.DEFAULT_TYPE):
    goodbye_text = """
👋 *¡Gracias por visitarnos!*

¡Ha sido un placer atenderte! Esperamos verte pronto nuevamente en *Mole Doña María*.

🌟 *No olvides:*
• Calificarnos en Google Maps
• Seguirnos en redes sociales
• Recomendarnos con tus amigos y familia

*¡Hasta pronto!* 😊🌶️

*Si necesitas algo más, escribe /start*
    """
    await update.message.reply_text(goodbye_text, parse_mode='Markdown')
    return SELECTING_ACTION

# Información del producto
async def product_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    product_text = """
ℹ️ *INFORMACIÓN DEL PRODUCTO*

🌶️ *Mole Doña María - Tradición Familiar*

*Ingredientes Principales:*
• Chile ancho, mulato y pasilla
• Chocolate orgánico de Oaxaca
• Especias naturales (canela, clavo, pimienta)
• Ajonjolí tostado
• Cacahuate natural
• 0% conservadores artificiales

*Beneficios:*
✅ 100% natural
✅ Sin colorantes artificiales  
✅ Sin conservadores
✅ Apto para vegetarianos (opción)
✅ Gluten free

*Valor Nutricional (por 100g):*
• Calorías: 180 kcal
• Proteína: 8g
• Grasas: 12g (grasas buenas)
• Carbohidratos: 15g

*¡Sabor auténtico de generación en generación!*
    """
    await update.message.reply_text(product_text, parse_mode='Markdown')
    return SELECTING_ACTION

# Puntos de venta
async def sales_points(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sales_text = """
📍 *PUNTOS DE VENTA*

🏪 *Tienda Principal:*
Calle Sabores Mexicanos #123
Colonia Centro, Ciudad de México
📞 Tel: (55) 1234 5678

🛒 *Sucursales:*
• *Norte:* Plaza del Sol, Av. Central #456
• *Sur:* Mercado Tradicional, Local 23
• *Este:* Centro Comercial Oriente, 2do piso
• *Oeste:* Plaza Occidente, Local 15

🛍️ *También nos encuentras en:*
• Supermercados La Comer
• Chedraui Selecto
• Mercados orgánicos
• Tiendas de especialidades

📦 *Compra Online:*
• www.moledonamaria.com
• Amazon México
• Mercado Libre

*¡Encuéntranos cerca de ti!* 🗺️
    """
    await update.message.reply_text(sales_text, parse_mode='Markdown')
    return SELECTING_ACTION

# Novedades
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    news_text = """
⭐ *NOVEDADES Y PROMOCIONES*

🎉 *¡NUEVO SABOR!* 
• Mole de Almendra - $160
  (Exclusiva combinación de almendras y especias)

🔥 *PROMOCIÓN DE LA SEMANA:*
• Combo Familiar + Postre gratis
• Válido hasta el domingo
• Solo menciona "PROMO BOT"

📦 *NUEVO SERVICIO:*
• ¡Ahora entregamos en todo México!
• Envíos gratis en compras mayores a $500

🎁 *PRÓXIMAMENTE:*
• Kits para hacer mole en casa
• Clases de cocina virtuales
• App móvil con descuentos exclusivos

*Síguenos en redes para más novedades!* 📱
    """
    await update.message.reply_text(news_text, parse_mode='Markdown')
    return SELECTING_ACTION

# Encuestas de productos
async def start_survey(update: Update, context: ContextTypes.DEFAULT_TYPE):
    survey_text = """
📊 *ENCUESTA DE SATISFACCIÓN*

¡Tu opinión es muy importante para nosotros! 
Califica tu experiencia con Mole Doña María:

⭐ *5 Estrellas* - Excelente
⭐⭐⭐⭐ *4 Estrellas* - Muy bueno  
⭐⭐⭐ *3 Estrellas* - Bueno
⭐⭐ *2 Estrellas* - Regular
⭐ *1 Estrella* - Malo

*Selecciona tu calificación:*
    """
    await update.message.reply_text(
        survey_text,
        reply_markup=survey_keyboard(),
        parse_mode='Markdown'
    )
    return SURVEY

async def process_survey(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rating = update.message.text
    
    if rating in ['⭐ 5 Estrellas', '⭐⭐⭐⭐ 4 Estrellas', '⭐⭐⭐ 3 Estrellas', 
                 '⭐⭐ 2 Estrellas', '⭐ 1 Estrella']:
        context.user_data['rating'] = rating
        
        thank_you_text = f"""
🙏 *¡Gracias por tu calificación!* {rating}

💬 *¿Te gustaría agregar algún comentario?*
Escribe tu sugerencia o experiencia (opcional):

*O selecciona "Volver al menú principal"*
        """
        await update.message.reply_text(
            thank_you_text,
            parse_mode='Markdown'
        )
        return SURVEY
    
    elif update.message.text == '🏠 Volver al menú principal':
        await start(update, context)
        return SELECTING_ACTION
    
    else:
        # Guardar comentario si es texto libre
        comment = update.message.text
        if 'rating' in context.user_data:
            # Aquí podrías guardar la calificación y comentario en una base de datos
            feedback_text = f"""
📝 *Feedback recibido:*
Calificación: {context.user_data['rating']}
Comentario: {comment}

¡Gracias por ayudarnos a mejorar! 💪
            """
            await update.message.reply_text(
                feedback_text,
                reply_markup=main_keyboard(),
                parse_mode='Markdown'
            )
            return SELECTING_ACTION
        else:
            await update.message.reply_text(
                "Por favor selecciona una calificación primero:",
                reply_markup=survey_keyboard()
            )
            return SURVEY

# Recomendaciones de productos
async def recommendations(update: Update, context: ContextTypes.DEFAULT_TYPE):
    recommendations_text = """
💡 *RECOMENDACIONES DEL CHEF*

🍽️ *Para principiantes:*
• Mole Tradicional + Pollo
• Perfecto balance de sabores

🌶️ *Para amantes del picante:*
• Mole Picante + Cerdo
• Acompañado de arroz extra

🥗 *Para vegetarianos:*
• Mole Verde + Queso panela
• Con tortillas de maíz azul

🎉 *Para ocasiones especiales:*
• Mix de 3 moles (250g cada uno)
• Ideal para degustar variedades

👨‍👩‍👧‍👦 *Para familias:*
• Combo Familiar + Agua de horchata
• Económico y delicioso

🍛 *Tips de preparación:*
• Calentar a fuego lento
• Revolver constantemente
• Servir con arroz esponjoso

*¡Buen provecho!* 😊🍴
    """
    await update.message.reply_text(recommendations_text, parse_mode='Markdown')
    return SELECTING_ACTION

# Recetas
async def recipes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    recipes_text = """
🍳 *RECETAS CON MOLE DOÑA MARÍA*

📋 *Mole Clásico con Pollo:*
• 500g de pollo
• 1 frasco de Mole Doña María
• 2 tazas de caldo de pollo
• Arroz y tortillas

*Preparación:*
1. Cocinar el pollo y desmenuzar
2. Mezclar el mole con caldo caliente
3. agregar el pollo y cocinar 10 min
4. Servir con arroz y tortillas

🌮 *Enchiladas de Mole:*
• 12 tortillas de maíz
• 1 frasco de mole
• Pollo desmenuzado
• Queso fresco y crema

*Preparación:*
1. Bañar tortillas en mole caliente
2. Rellenar con pollo, enrollar
3. Bañar con más mole y decorar

🍝 *Pasta con Mole:*
• 400g de pasta
• 1/2 frasco de mole
• 1 taza de crema
• Queso parmesano

*Preparación:*
1. Cocinar pasta al dente
2. Mezclar con mole y crema
3. Espolvorear queso

*¡Sé creativo en la cocina!* 👨‍🍳
    """
    await update.message.reply_text(recipes_text, parse_mode='Markdown')
    return SELECTING_ACTION

# Manejar mensajes de texto
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == '📦 Hacer pedido':
        return await start_order(update, context)
    elif text == '📖 Ver menú':
        return await show_menu(update, context)
    elif text == '🕒 Horarios de atención':
        return await show_hours(update, context)
    elif text == '📍 Puntos de venta':
        return await sales_points(update, context)
    elif text == 'ℹ️ Información del producto':
        return await product_info(update, context)
    elif text == '⭐ Novedades':
        return await news(update, context)
    elif text == '❓ Preguntas frecuentes':
        return await faqs(update, context)
    elif text == '📊 Encuestas':
        return await start_survey(update, context)
    elif text == '💡 Recomendaciones':
        return await recommendations(update, context)
    elif text == '🍳 Recetas':
        return await recipes(update, context)
    elif text == '👋 Despedida':
        return await goodbye(update, context)
    else:
        await update.message.reply_text(
            "¡Hola! Selecciona una opción del menú:",
            reply_markup=main_keyboard()
        )
        return SELECTING_ACTION

# Funciones existentes que se mantienen (start_order, process_order, show_menu, etc.)
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

async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu_text = """
🍽️ *MENÚ MOLE DOÑA MARÍA* 🌶️
*MOLES TRADICIONALES:*
• 🍯 Mole Tradicional - $120
• 🌶️ Mole Picante - $140  
• 🌿 Mole Verde - $130
*PLATILLOS ESPECIALES:*
• 🐔 Mole con Pollo - $180
• 🥩 Mole con Carne de Res - $200
• 🍖 Mole con Cerdo - $190
*EXTRAS:*
• 🍚 Arroz extra - $25
• 🫓 Tortillas (6 pzas) - $15
• 🥑 Guacamole - $40
• 🍹 Agua de horchata/jamaica - $30
*¡Todos incluyen arroz y tortillas!*
    """
    await update.message.reply_text(menu_text, parse_mode='Markdown')
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
            ],
            SURVEY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, process_survey)
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
