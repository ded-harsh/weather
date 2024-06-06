import requests

def get_weather(city):
    api_key = 'your_api_key'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    return response.json()
