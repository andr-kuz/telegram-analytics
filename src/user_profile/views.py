from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        return render(request=request, template_name='user_profile/index.html')
    else:
        return redirect('authentication:index')
