from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.handler, name='index'),
    path('logout', LogoutView.as_view(), name='logout'),
]
