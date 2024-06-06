from django.shortcuts import render
from .services import get_weather

def index(request):
    weather_data = None
    if 'city' in request.GET:
        city = request.GET['city']
        weather_data = get_weather(city)
    return render(request, 'weather/index.html', {'weather_data': weather_data})
