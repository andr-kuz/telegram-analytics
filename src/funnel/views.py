from django.shortcuts import render, redirect

def index(request):
    pass

def add(request):
    if request.user.is_authenticated:
        return render(request=request, template_name='funnel/add.html')
    return redirect('main:index')
