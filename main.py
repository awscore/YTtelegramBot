import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

users = {}

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     'Привет! Добро пожаловать, давай знакомиться, как тебя зовут?')
    users[chat_id] = {}
    bot.register_next_step_handler(message, save_username)


def save_username(message):
    chat_id = message.chat.id
    name = message.text
    users[chat_id] = name
    bot.send_message(chat_id, f'Отлично, {name}. Теперь укажи свою фамилию')




if __name__ == '__main__':
    print('Бот запущен!')
    bot.polling()

