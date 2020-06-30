from django.contrib import admin
from .models import Equipamento, Categoria, Grupo, Fabricante, Setor, Localizacao

@admin.register(Equipamento)
class Equipamento(admin.ModelAdmin):
    list_display = ('codigo', 'criado_em', 'modificado_em', 'usuario', 'categoria', 'fabricante', 'status','numero_serie', 'localizacao', 'setor', 'grupo', )
    search_fields = ('codigo', 'numero_serie', 'numero_patrimonio')
    list_filter = ('localizacao', 'setor', 'categoria')

@admin.register(Categoria)
class Categoria(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'criado_em', 'modificado_em', 'usuario')
    search_fields = ('nome', 'usuario')
    list_filter = ('criado_em', 'modificado_em')

@admin.register(Grupo)
class Grupo(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'criado_em', 'modificado_em', 'usuario')
    search_fields = ('nome', 'usuario')
    list_filter = ('criado_em', 'modificado_em')

@admin.register(Fabricante)
class Fabricante(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'criado_em', 'modificado_em', 'usuario')
    search_fields = ('nome', 'usuario')
    list_filter = ('criado_em', 'modificado_em')

@admin.register(Setor)
class Setor(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'criado_em', 'modificado_em', 'usuario')
    search_fields = ('nome', 'usuario')
    list_filter = ('criado_em', 'modificado_em')

@admin.register(Localizacao)
class Localizacao(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'criado_em', 'modificado_em', 'usuario')
    search_fields = ('nome', 'usuario')
    list_filter = ('criado_em', 'modificado_em')

