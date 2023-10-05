from config import TOKEN, BASE_URL
import requests

def pulling():
   count_message = 0
   while True:
       response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
       if count_message != len(response['result']):
           count_message = len(response['result'])
           message = response['result'][-1]
           user_id = message['message']['from']['id']
           requests.get(f"{BASE_URL}{TOKEN}/",
                        json={'method': 'kickChatMember', 'chat_id': '-1001620455362', 'user_id': 'id юзера'})


pulling()
#####



Методические указания
Урок 31.1. Введение в Telegram API
Задачи урока:
Введение в Telegram API

0. Подготовка к уроку

До начала урока преподавателю необходимо:
Просмотреть, как ученики справились с домашним заданием
Прочитать методичку

1. Введение в Telegram API

Учитель:  kickChatMember - Используйте этот метод, чтобы удалить пользователя из группы или супергруппы. В случае супергрупп пользователь не сможет вернуться в группу самостоятельно, используя ссылки для приглашения и т.д., Если сначала не будет снят запрет. Чтобы это сработало, бот должен быть администратором в группе. Возвращает значение True при успешном выполнении.

chat_id - Уникальный идентификатор целевой группы или имя пользователя целевой супергруппы (в формате @supergroupusername)
user_id - Уникальный идентификатор целевого пользователя

import requests

BASE_URL = 'https://api.telegram.org/bot'

TOKEN = '5580946066:AAH9SSwpAd_Pyp9pNkE9NrlD7DDZ53igeio'
ADMINS = [1865314469, ]


def pulling():
   count_message = 0
   while True:
       response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
       if count_message != len(response['result']):
           count_message = len(response['result'])
           message = response['result'][-1]
           user_id = message['message']['from']['id']
           requests.get(f"{BASE_URL}{TOKEN}/",
                        json={'method': 'kickChatMember', 'chat_id': 'id чата', 'user_id': 'id юзера'})


pulling()




unbanChatMember - Используйте этот метод, чтобы отменить блокировку ранее удаленного пользователя в супергруппе. Пользователь не вернется в группу автоматически, но сможет присоединиться по ссылке и т.д. Чтобы это сработало, бот должен быть администратором в группе. Возвращает значение True при успешном выполнении.

chat_id - Уникальный идентификатор целевой группы или имя пользователя целевой супергруппы (в формате @supergroupusername)
user_id - Уникальный идентификатор целевого пользователя


import requests

BASE_URL = 'https://api.telegram.org/bot'

TOKEN = 'Ваш токен'
ADMINS = [Ваш id, ]


def pulling():
   count_message = 0
   while True:
       response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
       if count_message != len(response['result']):
           count_message = len(response['result'])
           message = response['result'][-1]
           user_id = message['message']['from']['id']
           requests.get(f"{BASE_URL}{TOKEN}/",
                        json={'method': 'unbanChatMember', 'chat_id': 'id чата', 'user_id': 'id юзера'})


pulling()




Следующие методы позволяют изменить существующее сообщение в истории сообщений вместо отправки нового сообщения с результатом действия. Это наиболее полезно для сообщений со встроенной клавиатурой, использующих запросы обратного вызова, но также может помочь уменьшить беспорядок в разговорах с обычными чат-ботами.

Пожалуйста, обратите внимание, что в настоящее время редактировать сообщения можно только без reply_markup или с помощью встроенных клавиатур.

editMessageText - Используйте этот метод для редактирования текстовых сообщений, отправленных ботом или через бота (для встроенных ботов). При успешном выполнении возвращается отредактированное сообщение.

chat_id - Требуется, если не указан идентификатор inline_message_id. Уникальный идентификатор целевого чата или имя пользователя целевого канала (в формате @channelusername)
message_id - Требуется, если не указан идентификатор inline_message_id. Уникальный идентификатор отправленного сообщения
inline_message_id - Требуется, если не указаны chat_id и message_id. Идентификатор встроенного сообщения
text - Новый текст сообщения
parse_mode - Отправьте Markdown или HTML, если вы хотите, чтобы приложения Telegram отображали жирный, курсивный, текст фиксированной ширины или встроенные URL-адреса в сообщении вашего бота.
disable_web_page_preview - Отключает предварительный просмотр ссылок для ссылок в этом сообщении
reply_markup - Объект, сериализованный в формате JSON для встроенной клавиатуры.

editMessageCaption - Используйте этот метод для редактирования подписей сообщений, отправленных ботом или через бота (для встроенных ботов). При успешном выполнении возвращается отредактированное сообщение.

chat_id - Требуется, если не указан идентификатор inline_message_id. Уникальный идентификатор целевого чата или имя пользователя целевого канала (в формате @channelusername)
message_id - Требуется, если не указан идентификатор inline_message_id. Уникальный идентификатор отправленного сообщения
inline_message_id - Требуется, если не указаны chat_id и message_id. Идентификатор встроенного сообщения
caption - Новая подпись к сообщению
reply_markup -  Объект, сериализованный в формате JSON для встроенной клавиатуры.


editMessageReplyMarkup - Используйте этот метод для редактирования только разметки ответов сообщений, отправленных ботом или через бота (для встроенных ботов). При успешном выполнении возвращается отредактированное сообщение.
chat_id - Требуется, если не указан идентификатор inline_message_id. Уникальный идентификатор целевого чата или имя пользователя целевого канала (в формате @channelusername)
message_id - Требуется, если не указан идентификатор inline_message_id. Уникальный идентификатор отправленного сообщения
inline_message_id - Требуется, если не указаны chat_id и message_id. Идентификатор встроенного сообщения
reply_markup - Объект, сериализованный в формате JSON для встроенной клавиатуры.

У ботов есть помимо обычного еще и инлайн режим.
Инлайн-режим (inline mode) — это специальный режим работы бота, с помощью которого пользователь может использовать бота во всех чатах.
Выглядит это так: пользователь вводит юзернейм бота в поле для ввода сообщения. После юзернейма можно ещё записать запрос (текст до 256 символов).
Появляется менюшка с результатами. Выбирая результат, пользователь отправляет сообщение.
Инлайн-режим можно включить в BotFather, там же можно выбрать плейсхолдер вместо стандартного "Search..."
В группе можно запретить использовать инлайн всем или некоторым участникам. В официальных приложениях Телеграм это ограничение объединено с ограничением на отправку стикеров и GIF.

Когда пользователь вызывает инлайн-режим, бот не может получить никакую информацию о контексте, кроме информации о пользователе. Таким образом, бот не может узнать ни чат, в котором вызвали инлайн, ни сообщение, на которое пользователь отвечает.
Но зато если включить в BotFather настройку "Inline Location Data", то бот сможет видеть геопозицию пользователей, когда они используют инлайн (на мобильных устройствах). Перед этим у пользователей показывается предупреждение.

С инлайн режимом мы работать не будем, но знать что он существует вы должны.

InlineQuery - Этот объект представляет входящий встроенный запрос. Когда пользователь отправляет пустой запрос, ваш бот может вернуть некоторые результаты по умолчанию или трендовые результаты.

id - Уникальный идентификатор для этого запроса
from - Отправитель
location - Уникальный идентификатор для этого местоположения отправителя запроса, только для ботов, которые запрашивают местоположение пользователя
query - Текст запроса
offset - Смещение результатов, которые будут возвращены, может контролироваться ботом

answerInlineQuery - Используйте этот метод для отправки ответов на встроенный запрос. В случае успеха возвращается значение True.
Допускается не более 50 результатов на запрос.

inline_query_id - Уникальный идентификатор для ответа на запрос
results - Сериализованный в формате JSON массив результатов для встроенного запроса
cache_time - Максимальное время в секундах, в течение которого результат встроенного запроса может кэшироваться на сервере. Значение по умолчанию равно 300.
is_personal - Передайте значение True, если результаты могут быть кэшированы на стороне сервера только для пользователя, отправившего запрос. По умолчанию результаты могут быть возвращены любому пользователю, отправившему тот же запрос
next_offset - Передайте смещение, которое клиент должен отправить в следующем запросе с тем же текстом, чтобы получить больше результатов. Передайте пустую строку, если результатов больше нет или если вы не поддерживаете разбивку на страницы. Длина смещения не может превышать 64 байта
switch_pm_text - Если он передан, клиенты отобразят кнопку с указанным текстом, которая переключает пользователя в приватный чат с ботом и отправляет боту стартовое сообщение с параметром switch_pm_parameter
switch_pm_parameter - Параметр для начального сообщения, отправляемого боту при нажатии пользователем кнопки переключения

InlineQueryResult - Этот объект представляет один результат встроенного запроса. Клиенты Telegram в настоящее время поддерживают результаты следующих 19 типов:

InlineQueryResultCachedAudio
InlineQueryResultCachedDocument
InlineQueryResultCachedGif
InlineQueryResultCachedMpeg4Gif
InlineQueryResultCachedPhoto
InlineQueryResultCachedSticker
InlineQueryResultCachedVideo
InlineQueryResultCachedVoice
InlineQueryResultArticle
InlineQueryResultAudio
InlineQueryResultContact
InlineQueryResultDocument
InlineQueryResultGif
InlineQueryResultLocation
InlineQueryResultMpeg4Gif
InlineQueryResultPhoto
InlineQueryResultVenue
InlineQueryResultVideo
InlineQueryResultVoice

Более подробно о работе с inline режимом вы можете ознакомиться в официальной документации

 Ранее мы немного рассмотрели как работать через Bot Api без использования библиотек, но на сегодняшний день огромное количество различных библиотек, которые максимально удобно реализуют взаимодействие с Bot Api. Нам же остается изучить методы и классы какой либо библиотеки, для того чтобы начать работать.

Мы с вами начнем знакомство с библиотекой aiogram. В отличие от других библиотек aiogram - асинхронная библиотека.
Асинхронное программирование — это особенность современных языков программирования, которая позволяет выполнять операции, не дожидаясь их завершения.

Для начала давайте создадим каталог для бота, организуем там virtual environment (далее venv) и установим библиотеку aiogram

Теперь установим модуль:
pip install aiogram
Также нам понадобится библиотека python-dotenv для файлов конфигурации
pip install python-dotenv

Давайте создадим файл bot.py с базовым шаблоном бота на aiogram


import asyncio
import logging
from aiogram import Bot, Dispatcher, types

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="Ваш токен")
# Диспетчер
dp = Dispatcher(bot)


# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
   await message.answer("Hello!")


# Запуск процесса поллинга новых апдейтов
async def main():
   await dp.start_polling(bot)


if __name__ == "__main__":
   asyncio.run(main())




Первое, на что нужно обратить внимание: aiogram — асинхронная библиотека, поэтому ваши хэндлеры тоже должны быть асинхронными, а перед вызовами методов API нужно ставить ключевое слово await, т.к. эти вызовы возвращают корутины.

Под handler обычно подразумевается обработчик чего-то (каких-то событий, входящих соединений, сообщений и т.д.)

Корутина (coroutine) - подпрограмма (функция), которая может начинаться, приостанавливаться и завершаться в произвольный момент времени. Корутины описываются синтаксисом async/await

Диспетчер регистрирует функции-обработчики, дополнительно ограничивая перечень вызывающих их событий через фильтры. После получения очередного апдейта (события от Telegram), диспетчер выберет нужную функцию обработки, подходящую по всем фильтрам, например, «обработка сообщений, являющихся изображениями, в чате с ID икс и с длиной подписи игрек». Если две функции имеют одинаковые по логике фильтры, то будет вызвана та, что зарегистрирована раньше.

Чтобы зарегистрировать функцию как обработчик сообщений, нужно сделать одно из двух действий:
1. Навесить на неё декоратор, как в примере выше. С различными типами декораторов мы познакомимся позднее.
2. Напрямую вызвать метод регистрации у диспетчера или роутера.
Рассмотрим следующий код:

import asyncio
import logging
from aiogram import Bot, Dispatcher, types

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="Ваш токен")
# Диспетчер
dp = Dispatcher(bot)


# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
   await message.answer("Hello!")


# Хэндлер на команду /test1
@dp.message_handler(commands=["test1"])
async def cmd_test1(message: types.Message):
   await message.reply("Test 1")


# Хэндлер на команду /test2
async def cmd_test2(message: types.Message):
   await message.reply("Test 2")


# Запуск процесса поллинга новых апдейтов
async def main():
   await dp.start_polling(bot)


if __name__ == "__main__":
   asyncio.run(main())




Хэндлер cmd_test2 не сработает, т.к. диспетчер о нём не знает. Исправим эту ошибку и отдельно зарегистрируем функцию:


import asyncio
import logging
from aiogram import Bot, Dispatcher, types

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="Ваш токен")
# Диспетчер
dp = Dispatcher(bot)


# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
   await message.answer("Hello!")


# Хэндлер на команду /test1
@dp.message_handler(commands=["test1"])
async def cmd_test1(message: types.Message):
   await message.reply("Test 1")


# Хэндлер на команду /test2
async def cmd_test2(message: types.Message):
   await message.reply("Test 2")

dp.register_message_handler(cmd_test2, commands="test2")
# Запуск процесса поллинга новых апдейтов
async def main():
   await dp.start_polling(bot)


if __name__ == "__main__":
   asyncio.run(main())





Рассмотрим еще пример простого эхо бота

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



bot = Bot(token='Ваш токен')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
   await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
   await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
   await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
   executor.start_polling(dp)



 При работе бота неизбежно возникновение различных ошибок, связанных не с кодом, а с внешними событиями. Простейший пример: попытка отправить сообщение пользователю, заблокировавшему бота. Чтобы не оборачивать каждый вызов в try..except, в aiogram существует специальный хэндлер для исключений, связанных с Bot API.
Рассмотрим следующий пример кода, имитирующий задержку перед ответом пользователю:


@dp.message_handler(commands="block")
async def cmd_block(message: types.Message):
    await asyncio.sleep(10.0)
    await message.reply("Вы заблокированы")


За эти 10 секунд пользователь может успеть заблокировать бота со своей стороны и попытка вызвать метод reply приведёт к появлению исключения BotBlocked. Напишем специальный хэндлер для этого исключения


from aiogram.utils.exceptions import BotBlocked

@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True


Аналогично пишутся обработчики и на другие исключения. Таким образом, если одна и та же непредвиденная ситуация может возникнуть в различных хэндлерах, то можно вынести её обработку в отдельный хэндлер ошибок. Кода будет меньше, а оставшийся станет читабельнее.

Для того, чтобы сделать код чище и читабельнее, aiogram расширяет возможности стандартных объектов Telegram. Например, вместо bot.send_message(...) можно написать message.answer(...) или message.reply(...). В последних двух случаях не нужно подставлять chat_id, подразумевается, что он такой же, как и в исходном сообщении.
Разница между answer и reply простая: первый метод просто отправляет сообщение в тот же чат, второй делает "ответ" на сообщение из message:


@dp.message_handler(commands="answer")
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dp.message_handler(commands="reply")
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')


Более того, для большинства типов сообщений есть вспомогательные методы вида "answer_{type}" или "reply_{type}", например:


from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



bot = Bot(token='Ваш токен')
dp = Dispatcher(bot)


@dp.message_handler(commands="dice")
async def cmd_dice(message: types.Message):
   await message.answer_dice(emoji="🎲")


if __name__ == '__main__':
   executor.start_polling(dp)




Python является интерпретируемым языком с сильной, но динамической типизацией, поэтому встроенная проверка типов, как, например, в C++ или Java, отсутствует. Однако начиная с версии 3.5 в языке появилась поддержка подсказок типов, благодаря которой различные чекеры и IDE вроде PyCharm анализируют типы используемых значений и подсказывают программисту, если он передаёт что-то не то. В данном случае подсказка types.Message соообщает PyCharm-у, что переменная message имеет тип Message, описанный в модуле types библиотеки aiogram. Благодаря этому IDE может на лету подсказывать атрибуты и функции.

При вызове команды /dice бот отправит в тот же чат игральный кубик. Разумеется, если его надо отправить в какой-то другой чат, то придётся по-старинке вызывать await bot.send_dice(...). Но объект bot (экземпляр класса Bot) может быть недоступен в области видимости конкретной функции. К счастью, объект бота доступен во всех типах апдейтов: Message, CallbackQuery, InlineQuery и т.д. Предположим, вы хотите по команде /dice отправлять кубик не в тот же чат, а в канал с ID -100123456789. Перепишем предыдущую функцию:


from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



bot = Bot(token='Ваш токен')
dp = Dispatcher(bot)


@dp.message_handler(commands="dice")
async def cmd_dice(message: types.Message):
   await message.bot.send_dice(-100123456789, emoji="🎲")


if __name__ == '__main__':
   executor.start_polling(dp)





Всё хорошо, но если вдруг вы захотите поделиться с кем-то кодом, то придётся каждый раз помнить об удалении из исходников токена бота, иначе придётся его перевыпускать у @BotFather. Чтобы обезопасить себя, давайте перестанем указывать токен прямо в коде, а вынесем его как переменную окружения.
Замените следующие строчки из начала файла:


import logging
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="Ваш токен"


на эти:


import logging
from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from sys import exit

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)


Но теперь ваш бот не запустится, т.к. будет сразу завершаться с ошибкой Error: no token provided. Чтобы передать переменную окружения в PyCharm, откройте сверху раздел Run -> Edit Configurations и добавьте в окне Environment Variables переменную с именем BOT_TOKEN и значением токена.



Запустите снова бота и убедитесь, что он работает. Получившийся код можно смело сохранять в PyCharm в File Templates.

Дополнительно
Если на уроке остается время, то ученикам можно предложить начать прорешивать домашнее задание.

Домашняя работа
Задача 1
Написать бота с возможностью приветствия на команду /start от пользователя, а также вывод справки о боте по команде /help










