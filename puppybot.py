import logging
import os

import requests
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

load_dotenv()

secret_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

URL = 'https://api.thedogapi.com/v1/images/search?mime_types=gif'


def get_new_image():
    try:
        response = requests.get(URL)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = 'https://api.thecatapi.com/v1/images/search?mime_types=gif'
        response = requests.get(new_url)
    return response.json()[0].get('url')


def new_dog(update, context):
    chat = update.effective_chat
    context.bot.send_animation(chat.id, get_new_image())


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['Покажи ещё!']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}! Посмотри, какого пёсика я тебе нашёл!'.format(name),
        reply_markup=button
    )
    context.bot.send_animation(chat.id, get_new_image())


def main():
    updater = Updater(token=secret_token)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(MessageHandler(Filters.all, new_dog))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
