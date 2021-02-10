from django.urls import path
from .views import home,about,contact,portfolio,price,services

app_name = 'home'
urlpatterns = [
    path('', home,name = 'index'),
    path('about', about,name = 'about'),
    path('contact', contact,name = 'contact'),
    path('portfolio', portfolio,name = 'portfolio'),
    path('price', price,name = 'price'),
    path('services', services,name = 'services'),

]
