from django.shortcuts import render
from .request import api_request

# Create your views here.
def home(request):

   return render(request, 'main/main.html')

def info(request):
   data = api_request('nairobi')
   context = {
      'data': data['weather'],
      'city': data['name']
   }
   return render(request, 'main/data.html', context)