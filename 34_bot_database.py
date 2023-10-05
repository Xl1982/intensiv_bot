import sqlite3
import re
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from config import TOKEN
logging.basicConfig(level=logging.INFO)

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


# открываем файл со схемой базы данных и читаем его содержимое
with open('schema.sql', 'r') as f:
    schema = f.read()

# подключаемся к бзд и создаем курсор для выполнения запросов
conn = sqlite3.connect('user.db')
cursor = conn.cursor()
cursor.execute(schema)
conn.commit()

@dp.message_handler(regexp='сделал домашнее задание|дз сдал|сделал дз|аттестацию сдал|аттестацию залил|сдал аттестацию|атестацию сдал')
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or "Anonymous"


    # проверяем есть ли пользователь в базе данных
    cursor.execute("SELECT user_id, message_count FROM users WHERE user_id=?", (user_id,))
    user_data = cursor.fetchone()
    if user_data:
        # если пользователь существует увеличиваем счетчик на +1
        cursor.execute("UPDATE users SET message_count = message_count + 1 WHERE user_id=?", (user_id,))
        conn.commit()
        await message.answer(f'Ваши очки увеличились @{username}! Текущий счет: {user_data[1] + 1}')
    else:
        cursor.execute("INSERT INTO users (user_id, username, message_count) VALUES (?, ?, 1)", (user_id, username))
        conn.commit()
        await message.answer(f"@{username} Поздравляю! Вы только что заработали свой первый бал!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)




