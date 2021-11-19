from os import environ
import requests as rq


api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
def api_request(city_name):     
   response = rq.get(api_url.format(city_name, environ.get('API_KEY')))
   weather_data = response.json()
   print(weather_data)
   return  weather_data
   

