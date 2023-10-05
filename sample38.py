import logging
import time
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import ParseMode
from aiogram.utils import executor
from config import TOKEN
API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    non_existing_user = 11111
    try:
        await message.answer('Неправильно закрыт <b> тег <b>')
    except Exception as err:
        await message.answer(f'Не попало в error Handler. Ошибка {err}')


    try:
        await bot.send_message(chat_id=non_existing_user, text="несуществующий пользователь")
    except Exception as err:
        await message.answer(f'не попало в error handler. ошибка {err}')

    await message.answer('Не существует <fff>тега<fff>')
    logging.info('Это не выполнится, бот не ляжет')
    await message.answer('Hello')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
