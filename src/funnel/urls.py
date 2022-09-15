from django.urls import path, include
from . import views

app_name = 'funnel'

urlpatterns = [
    path('add', views.add, name='add'),
]
