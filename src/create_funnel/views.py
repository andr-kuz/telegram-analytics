from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        return render(request=request, template_name='create_funnel/index.html')
    return redirect('main:index')
