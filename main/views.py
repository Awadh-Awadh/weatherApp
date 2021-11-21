from django.shortcuts import render
from .request import api_request

# Create your views here.
def home(request):
   data = api_request('muranga')
   context = {
      'data': data
   }

   return render(request, 'main/main.html', context)