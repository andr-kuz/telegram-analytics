from django.urls import path, include
from . import views

app_name = 'create_funnel'

urlpatterns = [
    path('', views.index, name='index'),
]
