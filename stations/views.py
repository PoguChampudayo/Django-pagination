import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
        file_reader = list(csv.DictReader(f))
    pages = Paginator(file_reader, 10)   
    needed_page = request.GET.get('page', 1) 
    page = pages.get_page(needed_page)
    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
