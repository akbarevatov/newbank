from django.urls import path
from . import views
from rest_framework.authtoken import views as rest_views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('my_account/', views.my_account, name='my_account'),
    path('api_auth/', rest_views.obtain_auth_token, name='api_auth'),
]