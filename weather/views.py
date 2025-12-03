from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .service import fetch_weather_data
# from .service import weather_data

# Create your views here.
@api_view(['GET'])
def get_weather(request):
    city = request.GET.get('city', 'Lagos')
    weather_data = fetch_weather_data(city)
    return Response(weather_data)
