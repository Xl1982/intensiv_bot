import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import BoundFilter
from aiogram.types import ParseMode
from aiogram  import executor
from config import TOKEN
API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
from admin_filters import IsAdminFilter

dp.filters_factory.bind(IsAdminFilter)

@dp.message_handler(commands=['sleep'], is_admin=True)
async def admin_command(message: types.Message):
    await message.answer('Привет, админ')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
