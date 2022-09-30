from turtle import st
from django.shortcuts import render
import json
import urllib

# Create your views here.
def index(request):
    location = "Texas"
    context = {}
    if request.method == "POST":
        location = request.POST['city']
        try:
            api_resp = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+location+'&appid=1192085d7988d4cf3402be4cc6907621').read()
        # http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=1192085d7988d4cf3402be4cc6907621
            json_format = json.loads(api_resp)

            context = {
                "Location" : str(json_format["name"]),
                "Longitude": str(json_format['coord']['lon']),  
                "Latitude" : str(json_format['coord']['lat']) ,
                "Country": str(json_format['sys']['country']),
                "Temperature": str(json_format['main']['temp']) + ' K',
                "Pressure": str(json_format['main']['pressure']),
                "Humidity": str(json_format['main']['humidity']),
                "Weather": str(json_format['weather'][0]['description'])
            }
            print(context)
        except Exception as e:
            print(e) 
            context = {'Error': e}


    return render(request, 'index.html', {'Context': context})