from django.http import HttpResponse
from django.shortcuts import render


def index(requests):
    return HttpResponse('Успешно!')

# Create your views here.
