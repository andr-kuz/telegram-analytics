import json
import pdb
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from userbot.error_converter import error_converter

@login_required(login_url='authentication:index')
def index(request):
    pass

@login_required(login_url='authentication:index')
def add(request):
    error = ''
    response = {'success': {}, 'error': {}}
    actions = {'subscribe', 'reaction', 'pm', 'comment'}
    if request.method == 'POST' and 'json_data' in request.POST:
        json_string = request.POST['json_data']
        while True:
            try:
                json_dict = json.loads(json_string)
            except json.decoder.JSONDecodeError as r:
                error = r
                break
            if json_dict[0]['action'] != 'susbscribe':
                error = 'Первым шагом всегда должна быть подписка'
            response['error'] = error_converter(error)
        return JsonResponse(response)
    return render(request=request, template_name='funnel/add.html', context={'actions': actions})
