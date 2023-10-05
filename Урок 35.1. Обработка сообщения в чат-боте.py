Методические указания
Урок 35.1. Обработка сообщения в чат-боте
Задачи урока:
Обработка сообщения в чат-боте

0. Подготовка к уроку

До начала урока преподавателю необходимо:
Просмотреть, как ученики справились с домашним заданием
Прочитать методичку

1. Обработка сообщения в чат-боте

Учитель:  Ну что ж с вебхуками мы немного поработали, пора начать реализовывать и простеньких ботов, правда использовать мы будем пулинг и запускать на локальном компьютере.
Давайте создадим простого бота(пока ничего не делающего). Вынесем все необходимые переменные в отдельный файл config.py, в котором мы их будем подгружать из переменных окружения.

config.py
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')




bot.py

import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN

# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)



if __name__ == "__main__":
   # Запуск бота
   executor.start_polling(dp, skip_updates=True)




В данном случае мы создали заготовку бота, в котором вынесли токен в отдельный файл. Между прочим разбивать программу, на отдельные файлы, является хорошей практикой, так как код становится более читабельным и редактируемым.

Для начала давайте будем перехватывать сообщения с текстом Привет, а в ответ отправлять Привет username. Для этого нам достаточно указать в обработчике, что текст равен строке ‘Привет’


@dp.message_handler(text='Привет')
async def cmd_test1(message: types.Message):
   await message.reply(f"Привет {message.from_user.username}")




В примере мы перехватываем все сообщения, текст которых равен Привет.  В переменной message, которая приходит нам вместе с сообщением и имеет тип Message, хранятся все данные о сообщении и отправителе/чате/группе.

Выводить сообщения можно также используя специальное оформление(html, markdown)
В распоряжении у нас имеется три способа разметки текста: HTML, Markdown и MarkdownV2. Наиболее продвинутыми из них считаются HTML и MarkdownV2, «классический» маркдаун оставлен для обеспечения обратной совместимости и поддерживает меньше возможностей.
За выбор форматирования при отправке сообщений отвечает аргумент parse_mode, например:


@dp.message_handler(text='Привет')
async def cmd_test1(message: types.Message):
   await message.reply(f"Привет <i>{message.from_user.username}</i>", parse_mode=types.ParseMode.HTML)





@dp.message_handler(text='Привет')
async def cmd_test1(message: types.Message):
   await message.reply(f"Привет *{message.from_user.username}*", parse_mode=types.ParseMode.MARKDOWN_V2)




Если в боте повсеместно используется определённое форматирование, то каждый раз указывать аргумент parse_mode довольно накладно. К счастью, в aiogram можно передать необходимый тип прямо в объект Bot, а если в каком-то конкретном случае нужно обойтись без разметок, то просто укажите parse_mode="" (пустая строка):


bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

#с использованием разметки
@dp.message_handler(text='Привет')
async def cmd_test1(message: types.Message):
   await message.reply(f"Привет <b>{message.from_user.username}</b>")






bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

#без использования разметки
@dp.message_handler(text='Привет')
async def cmd_test1(message: types.Message):
   await message.reply(f"Привет <b>{message.from_user.username}</b>", parse_mode='')





Существует и более «программный» или даже «динамический» способ формирования сообщения. Для этого нужно импортировать модуль markdown из aiogram.utils, который, несмотря на название, поддерживает и HTML тоже. Далее вызовите функцию text(), в которую передайте произвольное число таких же вызовов функции text(). Тип форматирования определяется названием функции, а буква "h" в начале означает HTML, т.е. функция hbold() обрамляет переданный ей текст как жирный в HTML-разметке (<b>текст</b>). Аргумент sep определяет разделитель между кусками текста.


import aiogram.utils.markdown as fmt

@dp.message_handler(text='Привет')
async def cmd_test1(message: types.Message):
   await message.answer(
       fmt.text(
           fmt.text(fmt.hunderline("Яблоки"), ", вес 1 кг."),
           fmt.text("Старая цена:", fmt.hstrikethrough(50), "рублей"),
           fmt.text("Новая цена:", fmt.hbold(25), "рублей"),
           sep="\n"
       ), parse_mode="HTML"
   )





Помимо отправки с форматированием, Aiogram позволяет извлекать входящий текст как простое содержимое (plain text), как HTML и как Markdown. Сравнить можно на скриншоте ниже. Это удобно использовать, например, если вы хотите вернуть отправителю его сообщение с небольшими изменениями:


@dp.message_handler(text='Привет')
async def any_text_message(message: types.Message):
   await message.answer(message.text)
   await message.answer(message.md_text)
   await message.answer(message.html_text)
   # Дополняем исходный текст:
   await message.answer(
       f"<u>Ваш текст</u>:\n\n{message.html_text}", parse_mode="HTML"
   )




С использованием форматирования есть проблема: не в меру хитрые пользователи могут использовать спец. символы в именах или сообщениях, ломая бота. Впрочем, в aiogram существуют методы экранирования таких символов: escape_md() и quote_html(). Либо можно использовать упомянутые выше методы (h)bold, (h)italic и прочие:


@dp.message_handler(text='Привет')
async def any_text_message2(message: types.Message):
   await message.answer(f"Привет, <b>{fmt.quote_html(message.text)}</b>", parse_mode=types.ParseMode.HTML)
   # А можно и так:
   await message.answer(fmt.text("Привет,", fmt.hbold(message.text)), parse_mode=types.ParseMode.HTML)




Помимо обычных текстовых сообщений Telegram позволяет обмениваться медиафайлами различных типов: фото, видео, гифки, геолокации, стикеры и т.д. У большинства медиафайлов есть свойства file_id и file_unique_id. Первый можно использовать для повторной отправки одного и того же медиафайла много раз, причём отправка будет мгновенной, т.к. сам файл уже лежит на серверах Telegram. Это самый предпочтительный способ.
К примеру, следующий код заставит бота моментально ответить пользователю той же гифкой, что была прислана:


@dp.message_handler(content_types=[types.ContentType.ANIMATION])
async def echo_document(message: types.Message):
    await message.reply_animation(message.animation.file_id)


file_id уникален для каждого бота, т.е. переиспользовать чужой идентификатор нельзя. Однако в Bot API есть ещё file_unique_id. Его нельзя использовать для повторной отправки или скачивания медиафайла, но зато он одинаковый у всех ботов. Нужен file_unique_id обычно тогда, когда нескольким ботам требуется знать, что их собственные file_id односятся к одному и тому же файлу.
Кстати, про скачивание: aiogram предлагает удобный вспомогательный метод download() для загрузки небольших файлов на сервер, где запущен бот:


@dp.message_handler(content_types=[types.ContentType.DOCUMENT])
async def download_doc(message: types.Message):
    # Скачивание в каталог с ботом с созданием подкаталогов по типу файла
    await message.document.download()


# Типы содержимого тоже можно указывать по-разному.
@dp.message_handler(content_types=["photo"])
async def download_photo(message: types.Message):
    # Убедитесь, что каталог /tmp/somedir существует!
    await message.photo[-1].download(destination="/tmp/somedir/")


С выводом текста в сообщениях мы разобрались. Но как работают в целом хендлеры? Ведь обработка сообщений - одно из самых важных, если не самое важное.
Вернемся к нашему шаблону

import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt
from config import BOT_TOKEN

# Объект бота
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
   await message.answer(f"Привет, {message.from_user.full_name}")


if __name__ == "__main__":
   # Запуск бота
   executor.start_polling(dp, skip_updates=True)




Что же тут делает декоратор message_handler?
Открываем источник нажав на декораторе с зажатой клавишей CTRL и видим такое:




Декоратор вызывает функцию register_message_handler и передает в нее все условия (фильтры), что мы указали и callback (функцию, в которой мы хотим обрабатывать наше сообщение).
А что же происходит в функции register_message_handler?



Тут регистрируются наши условия (фильтры) и выполняется метод register у объекта message_handlers. То есть, если мы возьмем вместо декоратора просто функцию dp.register_message_handler - будет тот же результат, что и декоратором.
Давайте разберемся, что же это за функция register?





Есть некий класс Handler, у которого есть атрибут-список хендлеров, называется он self.handlers
И выполняя функцию register, мы добавляем наш HandlerObj, в котором будет нужная нам функция с нужными фильтрами, в список хендлеров этого типа (например message или callback_query).

Если посмотреть в объект Dispatcher, то увидим следующее:


У диспатчера есть набор атрибутов-хендлеров. Это и message_handlers, и edited_message_handlers и channel_post_handlers и другие. Это те самые объекты типа Handler, у которого есть список self.handlers, в который мы добавляем наши обработчики.
Теперь, когда нам понятно как регистрируются наши хендлеры, давайте глянем, что происходит, когда приходит апдейт.

У Dispatcher есть метод process_update, который проверяет тип апдейта, и выполняет функцию notify у нужного типа хендлеров.
Заходим в метод notify и видим:



1. Если на типа хендлеров установлен ключ миддлваря, то тригеррится функция pre_process_ у необходимого типа апдейтов.
2. Происходит итерация по ЗАРЕГИСТРИРОВАННЫМ хендлерам этого типа (например message). Тот самый список, в который делали append в объекте Handler.
3. Идет проверка на фильтры в каждом хендлере. Если все условия не выполняются - поднимается ошибка FilterNotPassed, и в этой строке она обрабатывается и происходит переход к следующему хендлеру.
4. Теперь, когда ошибка не случилась- фильтры подошли, триггерится уже миддлварь ключа process_
5.После чего выполняется та функция, которую мы зарегистрировали с нужными параметрами (переданными, как самим аиограмом, так и через миддлвари).

Давайте разберем каким образом мы можем работать с сообщениями, а конкретнее со встроенными фильтрами. Используя aiogram вы получаете множество возможностей, которых нет в других библиотеках, как например встроенные фильтры. Вместо того, чтобы писать func=lambda message: message.text=="Текст", как в pyTelegramBotApi, в aiogram вы пропишете просто text="Текст". Но это далеко не все. При этом встроенные фильтры постоянно добавляются.
Давайте посмотрим какие же у нас присутствуют фильтры.
Составим небольшой список всех фильтров
Command — проверка сообщения на команду
CommandHelp — проверка на команду /help
CommandPrivacy — проверка на команду /privacy
CommandSettings — проверка на команду /settings
CommandStart — проверка на команду /start
ContentTypeFilter — проверка типа контента
ExceptionsFilter — исключение для errors_handler
HashTag — обработка сообщений с #hashtag и $cashtags
Regexp — регулярное выражение для сообщений callback query
RegexpCommandsFilter — проверка команды регулярным выражением
StateFilter — проверка состояния пользователя
Text — фильтр текста. Работает на большинстве обработчиков
IDFilter — фильтр для проверки id чата или пользователя
AdminFilter — проверка на то, является ли пользователь администратором чата
IsReplyFilter — проверяет, что отправленное сообщение является ответом
IsSenderContact — проверяет, что пользователь отправил именно свой контакт
ForwardedMessageFilter — проверка на то, что сообщение переслано
ChatTypeFilter — проверка типа чата

Все стандартные фильтры подключаются на Dispatcher при его инициализации, при помощи приватного метода _setup_filters. Здесь мы можем сразу увидеть к каким из обработчиков применяются фильтры. Например первый подключаемый фильтр — StateFilter, который вы используете для работы с машиной состояний, подключается всем обработчикам кроме errors_handlers, poll_handlers и poll_answer_handlers, а ContentTypeFilter исключительно к сообщениям, которые содержат в update тип Message (т.к. только в нем есть content_type). Это следует из следующих строк:



Все command фильтры применяются исключительно на обработчики message_handler и edited_message_handler.
Может использоваться как аргумент обработчика commands. Т.е. вы можете использовать данный фильтр двумя способами:


@dp.message_handler(commands='myCommand', commands_ignore_caption=False)





from aiogram.dispatcher.filters import Command


@dp.message_handler(Command('myCommand', ignore_caption=False))




Наверное самый часто используемый фильтр — Command. Кроме аргумента commands он принимает prefixes, ignore_case, ignore_mention, ignore_caption.
prefixes — префиксы команды, т.е. то, с чего команда начинается. Самыми частыми префиксами являются стандартный "/", а также "!".
ignore_case — игнорировать регистр команды. Проверяется с помощью str.lower().
ignore_mention — игнорировать упоминание бота. По умолчанию False. Таким образом, когда бот получает команду с mention другого бота, он её не обрабатывает. Если передать True, в независимости от mention в /command@mention команда попадёт в обработчик, даже если это команда с упоминанием другого бота. Помните, что бот с включенным privacy mode не получит команду с упоминанием другого бота.
ignore_caption — игнорировать команды, которые написаны под изображением. По умолчанию True.

CommandStart - Этот фильтр, для проверки команды /start. Это фильтр Command, в который передаётся команда 'start', а остальные аргументы остаются по умолчанию. Фильтр CommandStart принимает лишь два аргумента:
deep_link — строка или регулярное выражение, для обработки deep_link.
encoded — обрабатывать закодированную ссылку deep_link (по умолчанию False).

from aiogram import types
from aiogram.dispatcher.filters import CommandStart


@dp.message_handler(filters.CommandStart(deep_link='deep_link'))
async def deep_link(msg: types.Message):
    await msg.answer('Да, знаем мы такое')

@dp.message_handler(filters.CommandStart())
async def command_start_handler(msg: types.Message):
    await msg.answer('Привет!')



Кроме обычного ответа на команду /start, этот фильтр также обрабатывает deep_link, для обработки deep_link. Мы ловим с его помощью ссылки с говорящим аргументом 'deep_link' (т.е ссылок вида https://t.me/{bot.username}?start=deep_link).

Фильтры CommandHelp, CommandPrivacy и CommandSettings не представляют из себя ничего особо интересного. Это просто фильтр Command с переданной в него командой 'help', 'privacy' или 'settings' соответственно. Особенность этих команд заключается в том, что это глобальные команды, наличие которые добавляет дополнительные кнопки в профиле бота.

ContentTypeFilter - Этот фильтр проверяет тип контента, будь то фото, текст или что-нибудь другое. Должен использоваться исключительно как аргумент content_types. По умолчанию проверяет на текст. Принимает либо строку, либо aiogram.types.ContentTypes (что строкой и является).


from aiogram import types
from aiogram.dispatcher import filters




@dp.message_handler(content_types='photo')
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def content_type_example(msg: types.Message):
    await msg.answer('Красиво 😍')




ExceptionsFilter - Фильтр, используемый в error_handlers. Принимает исключение. Работает исключительно в качестве аргумента по ключевому слову exception


from aiogram import types
from aiogram.utils import exceptions
from loguru import logger



@dp.errors_handler(exception=exceptions.BotBlocked)
async def bot_blocked_error(update: types.Update, exception: exceptions.BotBlocked):
    logger.exception(f'Bot blocked by user {update.message.from_user.id}')
    return True




Данный обработчик сработает, когда бот словит исключение BotBlocked. Здесь можно, например, удалять пользователя из базы данных, чтобы во время следующей рассылки не тратить время на данного пользователя.



Дополнительно
Если на уроке остается время, то ученикам можно предложить начать прорешивать домашнее задание.

Домашняя работа
Задача 1
Добавить в эхо бота возможность пересылки изображений, анимаций



