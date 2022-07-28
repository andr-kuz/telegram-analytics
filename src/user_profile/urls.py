from django.urls import path, include
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_funnel/', include('create_funnel.urls'))
]
