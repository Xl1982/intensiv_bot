import logging

from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram import types
from aiogram.dispatcher import filters
from config import TOKEN
API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE),commands='is_pm')
async def chat_type(msg: types.Message):
    await msg.answer('Это личка')


#
# @dp.message_handler(is_reply=True, commands='user_id')
# async def reply_filter_example(msg: types.Message):
#     await msg.answer(msg.reply_to_message.from_user.id)
#
#
#
# @dp.message_handler(filters.ForwardedMessageFilter(True))
#
# async def forwarded(msg: types.Message):
#     await msg.answer('Не пытайся меня обмануть это форвард')

#
#
# FORBIDDEN_PHRASE = ['01']
#
#
#
# SUPERUSER_IDS = '1120233842'
#
# @dp.message_handler(filters.IDFilter(chat_id=SUPERUSER_IDS))
# @dp.message_handler(chat_id=SUPERUSER_IDS)
# async def id_filter_example(msg: types.Message):
#     await msg.answer('Да, помню тебя')
#
#
#
#
# @dp.message_handler(filters.Text(contains=FORBIDDEN_PHRASE, ignore_case=True))
# async def text_example(msg: types.Message):
#     await msg.reply('Ответ!')
#
#
# @dp.message_handler(commands='set_state')
# async def set_state(msg: types.Message, state: FSMContext):
#     """Присваиваем пользователю состояние для теста"""
#     await state.set_state('example_state')
#     await msg.answer('Состояние установлено')
#
#
# @dp.message_handler(state='example_state')
# async def state_example(msg: types.Message, state: FSMContext):
#     await msg.answer('Ой всё, иди отсюда')
#     await state.finish()
#
#
#
#
#
#
# IMAGE_REGEXP = r'https://.+?\.(jpg|png|jpeg)'
# @dp.message_handler(filters.Regexp(IMAGE_REGEXP))
# async def regexp_example(msg: types.Message):
#     await msg.answer('Это пикча')
#
#
#
# @dp.message_handler(hashtags='аренда')
# async def hashtag_example(msg: types.Message):
#     await msg.answer('Это про аренду, введите сроки ')
#
# @dp.message_handler(hashtags='продажа')
# async def hashtag_example(msg: types.Message):
#     await msg.answer('АОпозпх')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
