import logging
import time
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from keyboards import kb1, kb3, kb4, kb5, ReplyKeyboardRemove
from config import TOKEN
API_TOKEN = TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    await message.reply('Привет', reply_markup=kb5)

@dp.message_handler(commands=['rm'])
async def rm(message: types.Message):
    await message.reply('Убираем клаву', reply_markup=ReplyKeyboardRemove())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
