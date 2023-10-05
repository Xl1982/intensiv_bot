import logging
import time
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from config import TOKEN
API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
#bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)
import aiogram.utils.markdown as fmt

# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)
#
# @dp.message_handler(text='Привет')
# async def cmd_test1(message: types.Message):
#     await message.reply(f'Привет <i>{message.from_user.username}</i>')

mess = f"""
Bold: 
*bold text* 
or 
__bold text__
Italic: _italic text_
Underline: __underline__
Strikethrough: ~strikethrough~
Single Line Code: `inline code`

"""
#
# @dp.message_handler(text='Пока')
# async def cmd_test2(message: types.Message):
#     await message.reply(f'{mess}*{message.from_user.username}*')
#
# @dp.message_handler(text='ping')
# async def cmd_test3(message: types.Message):
#    await message.answer(
#        fmt.text(
#            fmt.text(fmt.hunderline("Яблоки"), ", вес 1 кг."),
#            fmt.text("Старая цена:", fmt.hstrikethrough(50), "рублей"),
#            fmt.text("Новая цена:", fmt.hbold(25), "рублей"),
#            sep="\n"
#        ), parse_mode="HTML"
#    )
#
@dp.message_handler(content_types=[types.ContentType.ANIMATION])
async def echo_document(message: types.Message):
    await message.reply_animation(message.animation.file_id)

@dp.message_handler(content_types=[types.ContentType.DOCUMENT])
async def download_doc(message: types.Message):
    file_path = "media " + message.document.file_name
    await message.document.download(destination_dir=file_path)

@dp.message_handler(content_types='photo')
async def content_type_example(msg:types.Message):
    await msg.answer('Лайк')

from aiogram.utils import exceptions
from loguru import logger

@dp.errors_handler(exception=exceptions.BotBlocked)
async def bot_blocked(update: types.Update, exception: exceptions.BotBlocked):
    logger.exception(f'Бот блокирован юзером{update.message.from_user.id}')
    return True

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
