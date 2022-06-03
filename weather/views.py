from django.shortcuts import redirect, render, redirect
from .models import City
from .forms import CityForm
import requests
import os

def index(request):

    return render(request, 'weather/index.html')

def search(request):

    url = os.environ.get('url')
    
    err_msg = ''
    message = ''

    
    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()

            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()

                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist.'

            else:
                err_msg = 'City already ecists.'

        if err_msg:
            message = err_msg
        else:
            message = 'City was added!'

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon']
        }

        weather_data.append(city_weather)

    context = {
        'weather_data' : weather_data,
        'form' : form,
        'message' : message,
        }
    return render(request, 'weather/search.html', context)


def delete_city(request, city_name):

    City.objects.get(name=city_name).delete()

    return redirect('weather:search')

def delete_all(request):

    cities = City.objects.all()

    for city in cities:
        City.objects.get(name=city).delete()
    
    return redirect('weather:search')