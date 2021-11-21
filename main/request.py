from os import environ
import requests as rq

result_list = []
api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
def api_request(city_name):     
   response = rq.get(api_url.format(city_name, environ.get('API_KEY')))
   data = response.json()
   weather_info = data['weather']
   result_list.append(weather_info)
   return  result_list
   

