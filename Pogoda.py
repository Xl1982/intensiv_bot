import requests


def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Получаем температуру в градусах Цельсия
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather_description = data['weather'][0]['description']
        return {
            'temperature': main['temp'],
            'pressure': main['pressure'],
            'humidity': main['humidity'],
            'description': weather_description
        }
    else:
        return None


api_key = "ВАШ_КЛЮЧ_API"
city = "Moscow"
weather = get_weather(city, api_key)
print(weather)
