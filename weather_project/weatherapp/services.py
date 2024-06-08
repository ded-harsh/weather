# weatherapp/services.py

import requests
from django.conf import settings
from ipware import get_client_ip

def get_weather(location):
    api_key = settings.WEATHER_API_KEY
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(weather_url)
    return response.json()

def get_static_map(location):
    api_key = settings.GOOGLE_MAPS_API_KEY
    static_map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={location}&zoom=12&size=600x400&key={api_key}"
    return static_map_url

def get_location_from_ip(ip_address):
    location_url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(location_url)
    return response.json()
