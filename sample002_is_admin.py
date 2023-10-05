import logging
import time
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from config import TOKEN
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ADMINS = [1120233842]
API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


class AdminFilter(BoundFilter):
    async def check(self, message: types.Message):
        return message.from_user.id in ADMINS

dp.filters_factory.bind(AdminFilter)

@dp.message_handler(commands=['adminn'], user_id=ADMINS)
async def admin_command_handler(message: types.Message):
   await message.answer('Привет, админ!')


@dp.message_handler(commands=['start'])
async def admin_command_handler(message: types.Message):
    if message.from_user.id in ADMINS:
        keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("Админ панель", callback_data='admin_panel'))
        await message.answer("Привет, админ!Что хотите сделать", reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("Погугли сам", url="https://www.google.ru/"))
        await message.answer("Привет, чем могу помочь", reply_markup=keyboard)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
