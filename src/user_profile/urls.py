from django.urls import path, include
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('', views.index, name='user_profile')
]
