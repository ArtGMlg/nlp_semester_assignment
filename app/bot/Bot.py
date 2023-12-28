import telebot
from Methods import get_model_answer

API_TOKEN = '<api_token>'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"Привет, {message.from_user.first_name}!\nЯ рад, что ты мне написал\U0001F60A \nГотов общаться с тобой на любые темы, только не обижайся, если я отвечу что-то не так или буду ругаться.\U0001F97A\nЯ всего лишь небольшая модель для общения и много чего могу не знать")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    msg = bot.send_message(message.chat.id, '\U0001F4AC')
    ans = get_model_answer(message.text)
    bot.edit_message_text(chat_id = message.chat.id, message_id = msg.message_id, text = ans)
    

bot.infinity_polling()
