import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = "1979946920:AAEu9SuXey8_Zh9yaBeDij8yAF8LdlrZQ3E"

logging.basicConfig(level=logging. INFO)
bot = Bot(token=API_TOKEN)

dp = Dispatcher (bot)


questions = 'Какой язык мы сейчас изучаем?'

options = ['Python', 'Java', 'C++', '1C']
correct_answer = "Python"

@dp.message_handler(commands=['Victorina'])

async def Start_vic (message: types.Message):
    markup = InlineKeyboardMarkup(row_width=2)
    for option in options:
        markup.add(InlineKeyboardButton(option, callback_data=option))
    await message.reply(f'Вопрос {questions}', reply_markup=markup)

@dp.callback_query_handlers(lambda call: call.data==correct_answer)

async def Correct_otv (call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "Правильно")

@dp.callback_query_handler(lambda call: call.data in options and call.data != correct_answer)
async def wrong_answer_handler(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, f"Неправильно! Правильный ответ: {correct_answer}")

@dp.message_handler()

async def echo_mess (message: types.Message):

    await message.reply (message.text)

if __name__ == "__main__":
   executor.start_polling (dp, skip_updates=True)