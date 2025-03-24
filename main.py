import telebot
from telebot import types

TOKEN = "8150103995:AAHcMy8Oaa8fEHEF-wkkixlVNtQV9UZLKws"
bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "Раздача бесплатных Telegram Premium.\n\n"
        "Для получения премиума надо быть подписанным на канал не менее 7 дней"
    )

    # Создаем кнопку
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("🔰Подписаться🔰", url="https://t.me/+aQDoXBczEwhiNjBi")
    markup.add(button)

    # Отправляем сообщение с кнопкой
    bot.send_message(message.chat.id, text, reply_markup=markup)


# Запуск бота
print("Бот запущен!")
bot.polling()