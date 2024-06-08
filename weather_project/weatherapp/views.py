# weatherapp/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .services import get_weather, get_static_map, get_location_from_ip
from ipware import get_client_ip

def index(request):
    client_ip, is_routable = get_client_ip(request)
    if client_ip is None:
        location = 'Hyderabad'
    else:
        location_data = get_location_from_ip(client_ip)
        location = location_data.get('city', 'Hyderabad')
    
    location = request.GET.get('location', location)
    weather_data = get_weather(location)
    static_map_url = get_static_map(location)
    
    context = {
        'weather_data': weather_data,
        'static_map_url': static_map_url,
        'location': location
    }
    return render(request, 'weatherapp/index.html', context)
