from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import BoundFilter
from config import ADMINS

class IsGroup(BoundFilter): #
    async def check(self, message: types.Message):
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )

# class AdminFilter(BoundFilter): #определяется по апи телеграм кто является админом в канале
#     async def check(self, message: types.Message):
#         member = await message.chat.get_member(message.from_user.id)
#         return member.is_chat_admin()

class IsAdminFilter(BoundFilter): # фильтр определяет по списку админов из файла конфиг
    async def check(self, message: types.Message):
        return message.from_user.id in ADMINS

class IsPrivate(BoundFilter):
   async def check(self, message: types.Message):
       return message.chat.type == types.ChatType.PRIVATE
