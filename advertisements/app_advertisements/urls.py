from django.urls import path
from .views import index, top_sellers, advertisement_post, advertisement, login, profile, register


urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement_post/', advertisement_post, name='advertisement_post'),
    path('advertisement/', advertisement, name='advertisement'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
]
