import logging
import time
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
from config import TOKEN
API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
import asyncio


from aiogram.dispatcher.filters import Text


FORBIDDEN_PHRASE = (('Python', 'java'))


@dp.message_handler(Text(contains=FORBIDDEN_PHRASE, ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply('Ответ!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
