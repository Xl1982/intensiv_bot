import logging
import time
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from config import TOKEN
API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'hello'])
async def bot_start(message: types.Message):

   match message.text:
       case '/start':
           await message.answer(f"Бот запущен")

       case '/hello':
           await message.answer(f'Привет и я тебе рад, {message.from_user.full_name}')

       case '/help':
           await message.answer(f"Спасение утопающих{message.from_user.full_name}")

       case '/admin':
           await message.answer(f'Привет ты теперь админ, {message.from_user.full_name}')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
