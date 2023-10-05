import logging
import time
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode, BotCommand, BotCommandScopeDefault, BotCommandScopeChat
from aiogram.utils import executor
from config import TOKEN
API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def user_start(message: types.Message):
    await message.reply('Hello')
    await set_starting_commands(message.bot, message.from_user.id)


async def set_starting_commands(bot: Bot, chat_id: int):
    STARTING_COMMANDS= {
        'ru': [
            BotCommand('start', 'Начать заново'),
            BotCommand('get_commands', 'Получить список команд'),
            BotCommand('reset_commands', 'Сбросить команды')
        ],
        'en': [
            BotCommand('start', 'Restart bot'),
            BotCommand('get_commands', 'Retrieve command list'),
            BotCommand('reset_commands', 'Reset commands')
        ]
    }
    for language_code, commands in STARTING_COMMANDS.items():
        await bot.set_my_commands(
            commands=commands,
            scope=BotCommandScopeChat(chat_id),
            language_code=language_code)



@dp.message_handler(commands=['get_commands'])
async def message_get_command(message: types.Message):
   no_lang = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id))
   no_args = await message.bot.get_my_commands()
   ru_lang = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id), language_code='ru')


   def format_commands(commands_list):
       return '\n'.join(f"/{cmd.command}- {cmd.description}" for cmd in commands_list)

   await message.reply('\n'.join(
       format_commands(arg) for arg in (no_lang, no_args, ru_lang)
   ))





# async def set_default_commands(bot: Bot):
#     return await bot.set_my_commands(
#         commands=[
#             BotCommand("command_default_1", "Стандартная команда 1"),
#             BotCommand("command_default_2", "Стандартная команда 2"),
#             BotCommand("command_default_3", "Стандартная команда 3"),
#             BotCommand("start", "старт"),
#         ],
#         scope=BotCommandScopeDefault(),
#     )




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
