from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
import requests
from .serializers import VisitorSerializer
from django.conf import settings

geolocation_service = settings.IP2LOCATION_API_KEY
weather_api_service = settings.OPENWEATHER_MAP_API_KEY
class VistorView(generics.GenericAPIView):
    def get(self, request):
        visitor_name = request.query_params.get('visitor_name', 'Guest')
        client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
        
        location_response = requests.get(f'https://api.ip2location.io/?key={geolocation_service}&ip={client_ip}')
        location_data = location_response.json()
        city = location_data.get('city', 'Unknown')

        openweather_api_key = weather_api_service
        weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_api_key}&units=metric')
        weather_data = weather_response.json()
        temperature = weather_data['main']['temp'] if 'main' in weather_data else 'unknown'

        data = {
            "client_ip": client_ip,
            "location": city,
            "greeting": f"Hello, {visitor_name}! The temperature is {temperature} in {city}"
        }

        serializer = VisitorSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
visitor_view = VistorView.as_view()