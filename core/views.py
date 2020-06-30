from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound,JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import LoginForm
from .models import Equipamento

@login_required()
def index(request):
    return render(request, 'index.html')

@login_required()
def assets(request):
    return render(request, 'assets.html')

@login_required()
def get_assets_ajax(request):
    equipamentos = Equipamento.objects.all()
    data = [equipamento.listar_json() for equipamento in equipamentos]
    response = {'data': data}
    return JsonResponse(response, safe=False)

def user_login(request):

    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        valuenext = request.POST.get('next')
        user = form.login(request)
        if user:
            login(request, user)
            if valuenext is not None:
                return redirect('core:index')
            else:
                return redirect('core:index')
    return render(request, 'login.html', {'form': form})


@login_required()
def user_logout(request):
    logout(request)
    return redirect('core:index')
