from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('conta/sair', views.user_logout, name='logout'),
    path('conta/entrar', views.user_login, name='login'),
    path('ativos', views.assets, name='assets'),
    path('ativos/listar/json', views.get_assets_ajax, name="list_assets_json")
]
