from django.urls import path
from .views import home, info

urlpatterns = [
  path('', home, name = 'home'),
  path('weather-data', info, name='weather-data')

]