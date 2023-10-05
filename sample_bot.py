import logging
import re

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

API_TOKEN = '5999451135:AAEZNGUw2pGw-f9w5xicTEl3nPG48Qyczak'
logging.basicConfig(level = logging.INFO)

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(lambda message: re.search(r'http'|'www', message.text, re.IGNORECASE))
async def send_mess(message: types.Message):
    mess_1 = "Очень жаль"
    reply_text = mess_1
    await message.reply(reply_text, parse_mode=ParseMode.MARKDOWN)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)