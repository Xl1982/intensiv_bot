import time

from config import ADMINS, BASE_URL, TOKEN
import requests

# def pulling():
#     count_message = 0
#     while True:
#         response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
#         if count_message != len(response['result']):
#             count_message = len(response['result'])
#             message = response['result'][-1]
#             user_id = message['message']['from']['id']
#             if user_id in ADMINS:
#                 time.sleep(2)
#                 requests.get(f'{BASE_URL}{TOKEN}/sendContact?chat_id={user_id}&phone_number=45678&first_name=Jovan')
#
# pulling()
# def pulling():
#     count_massage = 0 # сколько обработанных сообщений
#     while True: # цикл постоянного обновления
#         response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json() # отправляем гет запрос на сервер апи тг
#         if count_massage != len(response['result']): # если количество сообщений не равно предыдущему
#             count_massage = len(response['result']) # обновляем каунтер на новое количество
#             message = response['result'][-1] # срез последнего сообщения
#             file_id = message['message']['video']['file_id'] # берем собщение извлекаем что это видео и извлекаем айди этого видео
#             user_id = message['message']['from']['id'] # извлекаем айди автора сообщение
#             if user_id in ADMINS: # если  юзер входит в список админо то
#                 requests.get(f'{BASE_URL}{TOKEN}/sendVideo?chat_id={user_id}&video={file_id}')
#
#
# pulling()


# def pulling():
#    count_message = 0
#    while True:
#        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
#        if count_message != len(response['result']):
#            count_message = len(response['result'])
#            message = response['result'][-1]
#            file_id = message['message']['voice']['file_id']
#            user_id = message['message']['from']['id']
#            if user_id in ADMINS:
#                requests.get(f'{BASE_URL}{TOKEN}/sendVoice?chat_id={user_id}&voice={file_id}')
#
# pulling()


"""
sendVoice - этот метод для отправки аудиофайлов, если вы хотите,
чтобы клиенты Telegram отображали файл в виде воспроизводимого голосового сообщения.
Чтобы это сработало, ваш звук должен быть в файле .ogg,
закодированном с помощью OPUS (другие форматы могут быть отправлены в виде аудио или документа)."""


# send location

def pulling():
    count_message = 0
    while True:
        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        if count_message != len(response['result']):
            count_message = len(response['result'])
            message = response['result'][-1]
            user_id = message['message']['from']['id']
            requests.get(f"{BASE_URL}{TOKEN}/",
                         json={'method': 'sendMessage', 'chat_id': f'{user_id}', 'text': 'Обычная клавиатура',
                               'reply_markup': {'keyboard': [[{'text': 'Отправить локацию', 'request_location': True},
                                                              {'text': 'Отправить контакт', 'request_contact': True}],
                                                             ], 'resize_keyboard': True, 'one_time_keyboard': True},
                               })


pulling()

