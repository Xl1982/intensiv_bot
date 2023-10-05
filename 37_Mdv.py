from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware # базовый класс для промежуточного ПО

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

block_users = ['id пользователя']

# создаем класс промежуточного ПО
class SomeMiddleware(BaseMiddleware):
    # перед обработкой любого обновления (до вызова обработчика)
   async def on_pre_process_update(self, update: types.Update, data: dict):
       print('on_pre_process_update')
       data['middleware_data'] = 'some update data' # дополнительные данные в словарь data
       if update.message: # если сообщение в обновлении есть
           await update.message.answer('on_pre_process_update') # отправляем ответное сообщение



    # после обработки любого обновления (после вызова обработчика)
   async def on_process_update(self, update: types.Update, data: dict):
       print(f'on_process_update, {data=}')


    # перед обработкой сообщения (до вызова обработчика сообщения)
   async def on_pre_process_message(self, message: types.Message, data: dict):
       print(f'on_pre_process_message, {data=}')
       data['middleware_data1'] = 'some message data1' # Добавляем дополнительные данные в словарь Data
       user_id = str(message.from_user.id) # получаем id пользователя отправившего сообщение
       print(user_id, user_id in block_users)
       data['is_blocked'] = user_id in block_users # проверяем заблокирован ли юзер
       # if user_id in block_users:
       #     await message.answer('ты в бане')
       #     raise CancelHandler()


   # после обработки сообщения
   async def on_process_message(self, message: types.Message, data: dict):
       print(f'on_process_message, {data=}')
       data['middleware_data2'] = 'some message data2' # добавляем доп данные в словарь Data
       user_id = str(message.from_user.id)
       data['user_id'] = user_id
       data['user'] = '123456' # пример добавления


   # после выполнения обработчика сообщения и всех промежуточных обработчиков
   async def on_post_process_message(self, message: types.Message, data_from_handler: list, data: dict):
       print(f'on_post_process_message, {data=}, {data_from_handler=}')
       data['middleware_data3'] = 'some message data3'


if __name__ == '__main__':
   dp.middleware.setup(SomeMiddleware())
   executor.start_polling(dp, skip_updates=True)


# Middleware - промежуточное ПО которое позволяет выполнять доп действия
# до и после обработки сообщений
# и других обновлений
# Например логирование, права доступа, бзд, кеш, ошибки, фильтрация данных



