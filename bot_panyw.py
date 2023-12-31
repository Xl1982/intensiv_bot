
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5691041366:AAEqoonM9RxkJd0hEqX_NCXZ9WRWEzVoMUE'


logging.basicConfig(level=logging.INFO)
proxy_url = 'http://proxy.server:3128'
bot = Bot(token=API_TOKEN, proxy=proxy_url)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_func(message: types.Message):
   await message.answer('Вы ввели команду /start')
   print('hello')


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)


"""Для работы с вебхуками мы можем использовать стандартный шаблон из официальной документации.
Как запустить бота с вебхуками мы рассмотрим в следующем занятии

шаблон
"""
import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

API_TOKEN = 'Ваш  токен'

# webhook settings
WEBHOOK_HOST = 'адрес сайта'
WEBHOOK_PATH = '/path/to/api'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'  # or ip
WEBAPP_PORT = 3001

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


async def on_startup(dp):
   await bot.set_webhook(WEBHOOK_URL)
   # insert code here to run it after start


async def on_shutdown(dp):
   logging.warning('Shutting down..')

   # insert code here to run it before shutdown

   # Remove webhook (not acceptable in some cases)
   await bot.delete_webhook()

   # Close DB connection (if used)
   await dp.storage.close()
   await dp.storage.wait_closed()

   logging.warning('Bye!')


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