import os
import django

# Configurar as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asset_manager.settings')
django.setup()

from core.models import Localizacao, Setor, Grupo, Categoria, Fabricante, Equipamento
from django.contrib.auth.models import User
import random
from faker import Faker

# Crie uma instância do Faker
fake = Faker()

# Função para criar dados fictícios
def criar_dados_ficticios(numero_de_registros=10):
    usuarios = User.objects.all()
    for _ in range(numero_de_registros):
        # Crie instâncias de objetos e preencha com dados fictícios
        localizacao = Localizacao.objects.create(
            usuario=random.choice(usuarios),
            nome=fake.word()
        )
        setor = Setor.objects.create(
            usuario=random.choice(usuarios),
            nome=fake.word()
        )
        grupo = Grupo.objects.create(
            usuario=random.choice(usuarios),
            nome=fake.word()
        )
        categoria = Categoria.objects.create(
            usuario=random.choice(usuarios),
            nome=fake.word()
        )
        fabricante = Fabricante.objects.create(
            usuario=random.choice(usuarios),
            nome=fake.word()
        )
        Equipamento.objects.create(
            usuario=random.choice(usuarios),
            localizacao=localizacao,
            setor=setor,
            grupo=grupo,
            categoria=categoria,
            fabricante=fabricante,
            modelo=fake.word(),
            numero_serie=fake.random_number(digits=10),
            numero_patrimonio=fake.random_number(digits=10),
            status=random.randint(0, 2),
            observacoes=fake.text()
        )

if __name__ == '__main__':
    criar_dados_ficticios()
