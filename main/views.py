from django.shortcuts import render
from .request import api_request

# Create your views here.
def home(request):

   return render(request, 'main/main.html')

def info(request):
   if request.method == "POST":
      query = request.POST.get('search')
      data = api_request(query)
   context = {
      'data': data['weather'],
      'city': data['name']
   }
   return render(request, 'main/data.html', context)