import datetime
import logging
import time
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from config import TOKEN, WEATHER_API
API_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.answer('Привет я бот погоды, введи назваание города')






@dp.message_handler()
async def get_weather(message: types.Message):

   code_to_smile = {
       "Clear": "Ясно \U00002600",
       "Clouds": "Ясно \U00002601",
       "Rain": "Дождь \U00002614",
       "Drizzle": "Дождь \U00002614",
       "Thunderstorm": "Гроза \U000026A1",
       "Snow": "Снег \U0001F328",
       "Mist": "Туман \U0001F32B"
   }
   try:
       r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={WEATHER_API}&units=metric')
       data = r.json()
       city = data['name']
       cur_weather = data['main']['temp']

       weather_description = data['weather'][0]['main']
       if weather_description in code_to_smile:
           wd = code_to_smile[weather_description]
       else:
           wd = 'Посмотри в окно сам'
       humidity = data['main']["humidity"]
       pressure = data['main']['pressure']
       sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
       sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
       length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - \
                           datetime.datetime.fromtimestamp(data['sys']['sunrise'])
       wind = data['wind']['speed']
       await message.answer(f'**{datetime.datetime.now().strftime("%d.%m.%Y %H:%M")}**\n'
             f'Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n'
             f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/c\n'
             f'Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n'
             f'Хорошего дня!')
   except Exception as err:
       await message.reply('Проверьте название города!')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
