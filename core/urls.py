from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('conta/sair', views.user_logout, name='logout'),
    path('conta/entrar', views.user_login, name='login'),
    path('equipamentos', views.assets, name='assets'),
    path('equipamentos/listar/json', views.assets_list_as_json, name="assets_list_json"),
    path('equipamento/cadastro/ajax', views.asset_register_ajax, name="asset_register_ajax"),
    path('equipamento/editar/<int:codigo>', views.asset_edit, name="asset_edit"),
    path('404/', views.error_404, name="error_404")
]
