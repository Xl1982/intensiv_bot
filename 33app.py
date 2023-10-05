import logging
import aiogram
import sqlite3


from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

#Создадим константы, которые нам потребуются
API_TOKEN = '1979946920:AAEu9SuXey8_Zh9yaBeDij8yAF8LdlrZQ3E'

# настройки вебхука
WEBHOOK_HOST = '2f21-178-156-86-240.ngrok-free.app'
WEBHOOK_PATH = '/2VQwecr7DWyqG5N864zxQeW0Xuk_39eQA9wTbc5MoveVWKkLj'
WEBHOOK_URL = f"https://{WEBHOOK_HOST}{WEBHOOK_PATH}"

# настройки веб сервера
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 3001

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
   await bot.send_message(message.chat.id, message.text)

async def on_startup(dp):
   await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
   logging.warning('Shutting down..')
   await bot.delete_webhook()
   logging.warning('Bye!')




@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
   return SendMessage(message.chat.id, 'Вы обратились к справке бота')


if __name__ == '__main__':
   start_webhook(
       dispatcher=dp,
       webhook_path=WEBHOOK_PATH,
       on_startup=on_startup,
       on_shutdown=on_shutdown,
       skip_updates=True,
       host=WEBAPP_HOST,
       port=WEBAPP_PORT,
   )
