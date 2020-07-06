from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound,JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, EquipamentoForm
from .models import Equipamento

@login_required()
def index(request):
    # retorna o template da página inicial
    return render(request, 'index.html')

@login_required()
def assets(request):
    # retorna o template da página de equipamentos
    return render(request, 'assets.html')

@login_required()
def asset_view(request, codigo):
    # busca o equipamento pelo codigo, caso não exista retorna o código de erro 404
    equipamento = get_object_or_404(Equipamento, pk=codigo)
    form = EquipamentoForm(instance=equipamento)
    # retorna o template da página de visualização do equipamento
    return render(request, 'asset.html', {"form":form})


@login_required()
def asset_update(request, codigo):
    # busca o equipamento pelo codigo, caso não exista retorna o código de erro 404
    equipamento = get_object_or_404(Equipamento, pk=codigo)
    response_data = {}
    if request.method == 'POST' and request.is_ajax():
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.usuario = request.user
            equipamento.localizacao = form.cleaned_data['localizacao']
            equipamento.setor = form.cleaned_data['setor']
            equipamento.grupo = form.cleaned_data['grupo']
            equipamento.categoria = form.cleaned_data['categoria']
            equipamento.fabricante = form.cleaned_data['fabricante']
            equipamento.modelo = form.cleaned_data['modelo']
            equipamento.numero_serie = form.cleaned_data['numero_serie']
            equipamento.numero_patrimonio = form.cleaned_data['numero_patrimonio']
            equipamento.status = form.cleaned_data['status']
            equipamento.observacoes = form.cleaned_data['observacoes']
            equipamento.save()
        else:
            pass
    else:
        return HttpResponseRedirect(error_404)

@login_required()
def get_assets_ajax(request):
    # obtém todos os equipamentos cadastrados
    equipamentos = Equipamento.objects.all()
    # atribuí todos os equipamentos à lista data
    data = [equipamento.listar_json() for equipamento in equipamentos]
    response = {'data': data}
    # retorna os dados obtidos no formato json
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

@login_required
def error_404(request, message):
    return render(request, '404.html', {"mensagem": message})


@login_required()
def user_logout(request):
    logout(request)
    return redirect('core:index')
