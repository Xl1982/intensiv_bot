from aiogram import Bot, executor, types
from aiogram.dispatcher import Dispatcher
from config import TOKEN
print(aiogram.__version__)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



if __name__ == '__main__':
    executor.start_polling(dp)