from django.urls import path, include
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.index, name='index'),
    path('funnel/', include('funnel.urls')),
    path('userbot/', include('userbot.urls')),
]
