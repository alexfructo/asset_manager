from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('conta/sair', views.user_logout, name='logout'),
    path('conta/entrar', views.user_login, name='login'),
    path('equipamentos', views.assets, name='assets'),
    path('equipamentos/listar/json', views.get_assets_ajax, name="list_assets_json"),
    path('equipamento/visualizar/<int:codigo>', views.asset_view, name="asset_view"),
    path('404/', views.error_404, name="error_404")
]
