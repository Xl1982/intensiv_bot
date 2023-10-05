import logging
import re
import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

API_TOKEN = '1979946920:AAEu9SuXey8_Zh9yaBeDij8yAF8LdlrZQ3E'
logging.basicConfig(level = logging.INFO)

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

with open('schema.sql', 'r') as f:
    schema = f.read()

conn = sqlite3.connect('user.db')
cursor = conn.cursor()
cursor.executescript(schema)
conn.commit()

@dp.message_handler()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or "Anonymous"

    cursor.execute("SELECT user_id, message_count FROM users WHERE user_id=?", (user_id,))
    user_data = cursor.fetchone()
    if user_data:
        cursor.execute("UPDATE users SET message_count = message_count + 1 WHERE user_id=?", (user_id,))
        conn.commit()
        await message.answer(f'Ваше очки увеличились @{username}! Текущий счет: {user_data[1] + 1}')
    else:
        cursor.execute("INSERT INTO users (user_id, username, message_count) VALUES (?, ?, 1)", (user_id, username))
        conn.commit()
        await message.answer(f'Пользователь @{username}Вы были добавленны в базу данных!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

