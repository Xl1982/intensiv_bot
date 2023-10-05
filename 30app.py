from config import ADMINS, BASE_URL, TOKEN
import requests

def pulling():
    count_message = 0
    while True:
        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        if count_message != len(response['result']):
            count_message = len(response['result'])

            message = response['result'][-1]
            file_id = message['message']['video']['file_id']
            user_id = message['message']['from']['id']
            if user_id in ADMINS:

                requests.get(f'{BASE_URL}{TOKEN}/sendVideo?chat_id={user_id}&video={file_id}')
pulling()