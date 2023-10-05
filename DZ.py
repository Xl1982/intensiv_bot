
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from config import TOKEN  # токен в конфиге
from aiogram.dispatcher import FSMContext
import re
import logging
logging.basicConfig(level=logging.INFO)
from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'], chat_type=types.ChatType.PRIVATE)
async def start_command(message: types.Message, state: FSMContext):
    welcome_text = "Привет"
    await message.answer(welcome_text)


@dp.message_handler(lambda message: re.search(r'когда урок|расписание', message.text, re.IGNORECASE))
async def when_is_the_class(message: types.Message):
    link_to_the_class = 'https://calendar.google.com/calendar/u/0/embed?src=49c6233cdd5d351149bc85a3cddaba3b7298782702399a401150d135d59fd8d9@group.calendar.google.com&ctz=Europe/Moscow'
    reply_text = f'ссылка на следующий урок: {link_to_the_class}'
    await message.reply(reply_text, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(lambda message: re.search(r'About', message.text, re.IGNORECASE))
async def about(message: types.Message):
    reply_text = f'я тестовый бот, созданный на интенсиве.\n Я умею скидывать расписание на интенсив. \n В дальнейшем будут еще функции'
    await message.reply(reply_text, parse_mode=ParseMode.MARKDOWN)
if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)