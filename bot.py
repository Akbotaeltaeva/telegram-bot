from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler

# Данные о продуктах
PRODUCTS = {
    "тоналка": [
        {"name": "Missha perfect cover", "price": "5000₸", "description": "Легкая текстура для всех типов кожи.", "image":"image/bb cream.jpg"},
        {"name": "ESTÉE LAUDER", "price": "20930₸", "description": "Матирующий эффект, подходит для жирной кожи.", "image": "image/estee lauder.jpg"},
    ],
    "пудра": [
        {"name": "Darling", "price": "4000₸", "description": "Удивительная мягкая кремовая текстура пудры.", "image": "image/darling.jpg"},
        {"name": "Givenchy prisme libre", "price": "20090₸", "description": "Рассыпчатая пудра для макияжа.", "image": "image/givenchy.jpg"},
    ],
    "тушь": [
        {"name": "MAYBELLINE NEW YORK lash sensational sky high", "price": "3500₸", "description": "Бесконечная длина и выразительный объем ресниц на весь день!", "image": "image/sky high.png"},
        {"name": "VIVIENNE SABO cabaret", "price": "1555₸", "description": "CABARET - настоящая легенда среди тушей!", "image": "image/cabaret.png"},
    ],
    "духи": [
        {"name": "YVES SAINT LAURENT libre flowers & flames", "price": "70590₸", "description": "Cоздавая яркий и в то же время успокаивающий аромат", "image": "image/духи лабре.jpeg"},
        {"name": "BANANA REPUBLIC tobacco & tonka bean", "price": "15000₸", "description": "Восточный гурманский аромат", "image": "image/духи табокка.jpeg"},
    ],
    "помада": [
        {"name": "VIVIENNE SABO le grand volume", "price": "3000₸", "description": "Увлажняющая помада с насыщенным цветом.", "image": "image/блеск.png"},
        {"name": "SHIK", "price": "8620₸", "description": "Матовая помада, стойкость до 12 часов.", "image": "image/шик.jpeg"},
    ],
    # Добавьте другие категории по аналогии...
}

# Команда /start
async def start(update: Update, context: CallbackContext) -> None:
    # Создаем кнопки категорий
    categories = ["Тоналка", "Пудра", "Тушь", "Духи", "Помада",]
    buttons = [
        [InlineKeyboardButton(category, callback_data=category.lower())] for category in categories
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(
        "Выберите категорию, чтобы посмотреть доступные продукты:", reply_markup=keyboard
    )

# Обработчик нажатий на кнопки категорий
async def category_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    # Получаем выбранную категорию из callback_data
    selected_category = query.data

    # Проверяем, есть ли продукты в этой категории
    if selected_category in PRODUCTS and PRODUCTS[selected_category]:
        products = PRODUCTS[selected_category]

        for product in products:
            # Отправляем продукт с изображением и описанием
            with open(product["image"], "rb") as photo:
                await context.bot.send_photo(
                    chat_id=query.message.chat_id,
                    photo=photo,
                    caption=f"Название: {product['name']}\nЦена: {product['price']}\nОписание: {product['description']}"
                )
    else:
        # Если продуктов нет или категория не найдена
        await query.edit_message_text(f"В категории '{selected_category}' пока нет доступных продуктов.")

# Главная функция
def main():
    # Замените на ваш действительный токен
    token = "7670141781:AAHTbPc4eRj9nH8yrFGWb9VFgOxjmhu9E4o"
    
    # Создание приложения
    application = Application.builder().token(token).build()
    
    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(category_handler))
    
    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()




