from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Advertisement
from .forms import AdvertisementModelForm
from django.urls import reverse


def index(requests):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(requests, 'index.html', context)


def top_sellers(requests):
    return render(requests, 'top-sellers.html')


def advertisement_post(requests):
    if requests.method == 'POST':
        form = AdvertisementModelForm(requests.POST, requests.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.user = requests.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementModelForm()
    context = {'form': form}
    return render(requests, 'advertisement-post.html', context)


def advertisement(requests):
    return render(requests, 'advertisement.html')


def login(requests):
    return render(requests, 'login.html')


def profile(requests):
    return render(requests, 'profile.html')


def register(requests):
    return render(requests, 'register.html')
