from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from userbot.models import Telegram
from userbot.telethon_userbot import Telethon
from userbot.error_converter import error_converter

persist_app = None

@login_required(login_url='authentication:index')
def index(request):
    userbots = Telegram.objects.filter(user_id=request.user.id)
    if not userbots:
        add(request)

@login_required(login_url='authentication:index')
def add(request):
    global persist_app
    error = ''
    if request.method == 'POST':
        response = {'success': {}, 'error': {}}
        api_id, api_hash, phone, code, password = request.POST['api_id'], request.POST['api_hash'], request.POST['phone'], request.POST['code'], request.POST['password']
        if not persist_app and api_id and api_hash and phone:
            app = Telethon(api_id, api_hash, phone)
            r = app.send_code_request()
            if isinstance(r, str):
                persist_app = app
            else:
                error = r
        elif persist_app and code:
            r = persist_app.sign_in(code, password)
            if r == True:
                session = persist_app.get_session_string()
                Telegram.objects.create(user_id=request.user.id, session_token=session)
                persist_app.exit()
            else:
                error = r
        else:
            error = 'Введите все данные'
        response['error'] = error_converter(error)
        return JsonResponse(response)
    return render(request=request, template_name='userbot/phone_and_token.html')
