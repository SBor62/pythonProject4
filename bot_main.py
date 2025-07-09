import telebot
from telebot.types import Message
import requests

API_URL = "http://127.0.0.1:8000/api"

BOT_TOKEN = "7973269831:AAFUzw4MjXR8HyJ9nbvjvzneDtvqZXxJFoQ"

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    data = {
        "user_id": message.from_user.id,
        "username": message.from_user.username
    }
    response = requests.post(API_URL + "/register/", json=data)
    if response.status_code == 200:
        bot.send_message(message.chat.id, f"Вы успешно зарегистрированы! Ваш уникальный номер: {response.json()['user_id']}")
    else:
        bot.send_message(message.chat.id, f"Произошла ошибка при регистрации!")


@bot.message_handler(commands=['myinfo'])
def user_info(message: Message):
    userid = message.from_user.id

    response = requests.get(f"{API_URL}/user/{userid}/")
    if response.status_code == 200:
        user_data = response.json()
        bot.reply_to(message, f"Ваша регистрация:\n\n{user_data}")
    elif response.status_code == 404:
        bot.send_message(message.chat.id, text="Вы не зарегистрированы!")
    else:
        bot.send_message(message.chat.id, f"Непредвиденная ошибка!:  {response.status_code}")


if __name__ == "__main__":
    bot.polling(none_stop=True)
