from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, EquipamentoForm
from .models import Equipamento


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
    return redirect('core:login')


@login_required()
def index(request):
    return render(request, 'index.html')


@login_required
def error_404(request, message):
    return render(request, '404.html', {"message": message})


@login_required()
def assets(request):
    return render(request, 'assets.html')


@login_required()
def assets_list_as_json(request):
    equipamentos = Equipamento.objects.all()
    data = [equipamento.listar_json() for equipamento in equipamentos]
    response = {'data': data}
    return JsonResponse(response, safe=False)


@login_required()
def asset_register(request):
    form = EquipamentoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            form.save()
            message = 'Cadastro realizado com sucesso!'
            return redirect(asset_edit(request, codigo=codigo, message=message))
    return render(request, 'asset_register.html', {"form": form})

@login_required()
def asset_edit(request, codigo, message=None):
    equipamento = get_object_or_404(Equipamento, pk=codigo)
    form = EquipamentoForm(instance=equipamento)
    return render(request, 'asset_edit.html', {"form": form})
