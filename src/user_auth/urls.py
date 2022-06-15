from django.urls import path, include
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('login', views.handler, name='login'),
    path('logout', views.log_out, name='logout'),
]
