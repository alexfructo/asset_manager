from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, EquipamentoForm
from .models import Equipamento, Localizacao, Setor, Grupo, Categoria, Fabricante


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
    form = EquipamentoForm()
    localizacao = Localizacao.objects.all()
    setor = Setor.objects.all()
    grupo = Grupo.objects.all()
    categoria = Categoria.objects.all()
    fabricante = Fabricante.objects.all()
    context = {
        "localizacao": localizacao,
        "setor": setor,
        "grupo": grupo,
        "categoria": categoria,
        "fabricante": fabricante,
        "form": form,
    }
    return render(request, 'assets.html', context)


@login_required()
def assets_list_as_json(request):
    if request.method == 'GET':
        equipamentos = Equipamento.objects.all()
        if request.GET.get('localizacao', False):
            equipamentos = equipamentos.filter(
                localizacao=request.GET.get('localizacao', False))
        if request.GET.get('setor', False):
            equipamentos = equipamentos.filter(
                setor=request.GET.get('setor', False))
        if request.GET.get('grupo', False):
            equipamentos = equipamentos.filter(
                grupo=request.GET.get('grupo', False))
        if request.GET.get('categoria', False):
            equipamentos = equipamentos.filter(
                categoria=request.GET.get('categoria', False))
        if request.GET.get('fabricante', False):
            equipamentos = equipamentos.filter(
                fabricante=request.GET.get('fabricante', False))
        if request.GET.get('status', False):
            equipamentos = equipamentos.filter(
                status=request.GET.get('status', False))

        data = [equipamento.listar_json() for equipamento in equipamentos]
        response = {'data': data}
        return JsonResponse(response, safe=False)
    else:
        equipamentos = Equipamento.objects.all()
        data = [equipamento.listar_json() for equipamento in equipamentos]
        response = {'data': data}
        return JsonResponse(response, safe=False)


@login_required()
def asset_register_ajax(request):
    if request.method == 'POST' and request.is_ajax():
        form = EquipamentoForm(request.POST or None)
        if form.is_valid():
            equipamento = Equipamento(
                usuario = request.user,
                localizacao = form.cleaned_data['localizacao'],
                grupo = form.cleaned_data['grupo'],
                setor = form.cleaned_data['setor'],
                categoria = form.cleaned_data['categoria'],
                fabricante = form.cleaned_data['fabricante'],
                status = form.cleaned_data['status'],
                numero_serie = form.cleaned_data['numero_serie'],
                numero_patrimonio = form.cleaned_data['numero_patrimonio'],
                observacoes = form.cleaned_data['observacoes'],
            )
            equipamento.save()
            data = {
                "success": True,
                "message":"Cadastro realizado com sucesso.",
            }
            return JsonResponse(data, status=200)
        else:
            data = {
                "success": False,
                "message": dict(form.errors.items()),
            }
            return JsonResponse(data, status=200)
                

@login_required()
def asset_edit(request, codigo, message=None):
    equipamento = get_object_or_404(Equipamento, pk=codigo)
    form = EquipamentoForm(instance=equipamento)
    return render(request, 'asset_edit.html', {"form": form})
