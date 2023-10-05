import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TOKEN
API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
from aiogram.dispatcher.filters import   Command
from Configi.filters import IsGroup,  IsPrivate

@dp.message_handler(IsPrivate(), Command(commands='private'))
async def start_bot(message: types.Message):
   await message.answer('Личный чат')


@dp.message_handler(IsGroup(), Command(commands='group'))
async def start_bot(message: types.Message):
   await message.answer('Групповой чат')







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
