import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from aiogram import Bot, Dispatcher, types
from config import TOKEN, CHAT_ID

API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def send_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Кнопка 1", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Кнопка 2", callback_data="button2")
    keyboard.add(button1, button2)
    await bot.send_message(CHAT_ID, "Выберите кнопку:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"Вы выбрали: {callback_query.data}")


if __name__ == '__main__':
    scheduler = AsyncIOScheduler()
    trigger = CronTrigger(hour=15, minute=3, second=0)
    scheduler.add_job(send_keyboard, trigger=trigger)
    scheduler.start()
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
