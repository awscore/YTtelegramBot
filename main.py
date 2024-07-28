import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     'Привет! Добро пожаловать, помочь скачать видео из Ютуб?')




if __name__ == '__main__':
    print('Бот запущен!')
    bot.polling()

