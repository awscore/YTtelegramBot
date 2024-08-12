import telebot
from telebot import types
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

users = {}

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Help'))
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     f'Отправь мне ссылку на видео из ютуб, например \n'
                     f'https://www.youtube.com/watch?v=urEndMm4dp0&t=14s', disable_web_page_preview=True,
                     reply_markup=markup)
    users[chat_id] = {}
    bot.register_next_step_handler(message)


# def save_username(message):
#     chat_id = message.chat.id
#     name = message.text
#     users[chat_id] = name
#     bot.send_message(chat_id, f'Отлично, {name}. Теперь укажи свою фамилию')




if __name__ == '__main__':
    print('Бот запущен!')
    bot.polling()

