from os import environ
import requests as rq


api_url = "api.openweathermap.org/data/2.5/weather?q={}&appid={}"

def api_request(city_name, api):
   result_list = []
   data = rq.get(api_url.format(city_name, environ.get('API_KEY')))
   weather_data = data.json()
   result_list.append(weather_data)
   return  result_list
   

