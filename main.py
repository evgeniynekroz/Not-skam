import telebot
from telebot import types
import threading
import time

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


# Функция для рассылки сообщения каждые 15 минут
def spam_premium():
    while True:
        try:
            text = "Забирай свой Telegram Premium. Осталось мало времени!"
            # Рассылает сообщение всем активным чатам (если база чатов будет добавлена)
            for chat_id in active_chats:
                bot.send_message(chat_id, text)
            
            # Ждем 15 минут (900 секунд)
            time.sleep(900)
        
        except Exception as e:
            print(f"Ошибка в рассылке: {e}")
            time.sleep(10)


# Сохраняем всех, кто написал боту
active_chats = set()

@bot.message_handler(func=lambda message: True)
def save_chat(message):
    active_chats.add(message.chat.id)


# Запускаем бота
print("Бот запущен!")
threading.Thread(target=spam_premium).start()
bot.polling()