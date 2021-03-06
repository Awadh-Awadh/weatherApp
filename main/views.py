from django.shortcuts import get_object_or_404, render,redirect
from .request import api_request

# Create your views here.
def home(request):

   return render(request, 'main/main.html')

def info(request):
   none = None
   query = request.POST.get('search')
   if query == '' :
      return redirect('weather-data')
   data = api_request(query)
   context = {
      'data':data,
      'info': data['weather'],
      'city': data['name'],
      'temperature': data['main']['temp'] - 273,
      'wind' : data['wind']['speed'],
      'humidity': data['main']['humidity'],
      'pressure' : data['main']['pressure'],
      'country' : data['sys']['country'],
      'name' : None,
      
   }
   print(data)
      
   return render(request, 'main/data.html', context)