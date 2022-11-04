from django.shortcuts import render, redirect
from userbot.models import Telegram
from django.contrib.auth.decorators import login_required

@login_required(login_url='authentication:index')
def index(request):
    userbots = len(Telegram.objects.filter(user_id=request.user.id))
    return render(request=request, template_name='profile/index.html', context={'userbots': userbots})
