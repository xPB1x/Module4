from django.http import HttpResponse
from django.shortcuts import render
from .models import Advertisement


def index(requests):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(requests, 'index.html', context)


def top_sellers(requests):
    return render(requests, 'top-sellers.html')