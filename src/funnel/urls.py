from django.urls import path, include
from . import views

app_name = 'funnel'

urlpatterns = [
    path('', views.add, name='add'),
]
