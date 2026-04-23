from django.urls import path
from . import views

app_name = 'currency'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/', views.currency_api, name='currency_api'),
    path('exchange_api/', views.exchange_api, name='exchange_api'),
]