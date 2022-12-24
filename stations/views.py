from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, 'r') as f:
        bus_stations = f.readlines()
    pages = Paginator(bus_stations, 10)   
    page = request.GET.get('page', 1) 
    context = {
         'bus_stations': pages,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
