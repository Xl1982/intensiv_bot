import logging
import time
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from config import TOKEN
import aiogram.utils.markdown as fmt
API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(text='Привет')
async def cmd_test(message: types.Message):
    await message.reply(f"Привет *{message.from_user.username}*")


@dp.message_handler(text='Еда')
async def cmd_test1(message: types.Message):
   await message.answer(
       fmt.text(
           fmt.text(fmt.hunderline("Яблоки"), ", вес 1 кг."),
           fmt.text("Старая цена:", fmt.hstrikethrough(50), "рублей"),
           fmt.text("Новая цена:", fmt.hbold(25), "рублей"),
           sep="\n"
       ), parse_mode="HTML"
   )
from aiogram.utils import exceptions
from loguru import logger

@dp.errors_handlers(exception=exceptions.BotBlocked)
async def bot_block(update: types.Update, exception: exceptions.BotBlocked):
    logger.exception(f"bot block{update.message.from_user.id}")
    return True

@dp.message_handler(text='Поля')
async def any_text_message(message: types.Message):
    await message.answer(message.text)
    await message.answer(message.md_text)
    await message.answer(message.html_text)
    await message.answer(
        f" <u>Ваш текст</u> :\n\n{message.html_text}",parse_mode="HTML"
    )

@dp.message_handler(content_types=[types.ContentType.DOCUMENT])
async def echo_animation(message: types.Message):
    await message.document.download()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
