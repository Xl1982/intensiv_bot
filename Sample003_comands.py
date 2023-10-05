import logging
import time
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode, BotCommandScopeDefault, BotCommand
from aiogram.utils import executor
from config import TOKEN
API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text

@dp.message_handler(commands='reset')
async def user_reset(message: types.Message):
    await reset_commands(bot)
    await message.reply("Commands have been reset to default.")


async def reset_commands(bot: Bot):
    return await bot.set_my_commands([])







@dp.message_handler(commands='start')
async def user_start(message: types.Message):
   await message.reply('Hello')
   await set_default_commands(bot)





async def set_default_commands(bot: Bot):
   return await bot.set_my_commands(
       commands=[
           BotCommand('command_default_1', 'Стандартная команда 1'),
           BotCommand('command_default_2', 'Стандартная команда 2'),
           BotCommand('command_default_3', 'Стандартная команда 3'),
       ],
       scope=BotCommandScopeDefault(),
   )




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
