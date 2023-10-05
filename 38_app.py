import logging
import sqlite3
import time
from venv import logger

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from config import TOKEN
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ADMINS = [1120233842]
API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


class Database:
    # конструктор класса, который вызывается при создании объекта класса
    def __init__(self, path_to_db='test.db'):
        # присвоение атрибуту path значение к пути bsd
        self.path_to = path_to_db


    @property # декоратор превращающий метод в свойстов, к которому можно обратиться без скобок
    def connection(self):
        return sqlite3.connect(self.path_to_db) # установка подключения к бзд

    # метод выполнения SQL запросов
    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        # если параметры не указаны, присвоен пустой кортеж
        if not parameters:
            parameters = tuple()

        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None # инициал переменной для данных
        cursor.execute(sql, parameters) # выполнение sql запроса
        if commit: #есил нужно сохранить изменения в базе данных
            connection.commit()

        if fetchone: # если нужно получить одну запись из резултата запроса
            data = cursor.fetchone()

        if fetchall: # если все нужны записи
            data = cursor.fetchall()

        connection.close() # закрываем бзд

        return data # ретрн результ


    # метод для создания таблцы Юзеры в бзд
    def create_table_users(self):
        sql = """
        CREATE TABLE Users(
        id int NOT NULL,
        name varchar(255) NOT NULL,
        email varchar(255),
        PRIMARY KEY (id)
        );
        """
        return self.execute(sql)

    def add_user(self, id: int, name: str, email: str = None):
        sql = "INSERT INTO Users(id, name, email) VALUES  (?, ?, ?)"
        parameters = (id, name, email)
        self.execute(sql, parameters=parameters, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f'{item} = ?' for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_email(self, email, id):
        sql = "UPDATE Users SET email=? WHERE id=?"
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_all_users(self):
        self.execute("DELETE FROM Users WHERE TRUE")




class AdminFilter(BoundFilter):
    async def check(self, message: types.Message):
        return message.from_user.id in ADMINS




dp.filters_factory.bind(AdminFilter)

@dp.message_handler(commands=['adminn'], user_id=ADMINS)
async def admin_command_handler(message: types.Message):
   await message.answer('Привет, админ!')


@dp.message_handler(commands=['start'])
async def admin_command_handler(message: types.Message):
    if message.from_user.id in ADMINS:
        keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("Админ панель", callback_data='admin_panel'))
        await message.answer("Привет, админ!Что хотите сделать", reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("Погугли сам", url="https://www.google.ru/"))
        await message.answer("Привет, чем могу помочь", reply_markup=keyboard)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
