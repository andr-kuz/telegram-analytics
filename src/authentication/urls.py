from django.urls import path, include
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.handler, name='index'),
    path('logout', views.log_out, name='logout'),
]
