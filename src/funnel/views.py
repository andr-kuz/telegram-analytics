from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='authentication:index')
def index(request):
    pass

@login_required(login_url='authentication:index')
def add(request):
    return render(request=request, template_name='funnel/add.html')
