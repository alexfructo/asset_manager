# Generated by Django 3.0.7 on 2020-06-24 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('modelo', models.CharField(blank=True, max_length=100, null=True)),
                ('numero_serie', models.CharField(blank=True, max_length=32, null=True)),
                ('numero_patrimonio', models.CharField(blank=True, max_length=32, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Armazenado'), (1, 'Alocado'), (2, 'Descartado')], default=0)),
                ('item_unico', models.BooleanField(default=False)),
                ('quantidade', models.IntegerField(default=0)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Categoria')),
            ],
            options={
                'ordering': ['categoria', 'fabricante'],
            },
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Movimento',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Armazenado'), (1, 'Alocado'), (2, 'Descartado')], default=0)),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Equipamento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['criado_em'],
            },
        ),
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.AddField(
            model_name='equipamento',
            name='fabricante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Fabricante'),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Grupo'),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='localizacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Localizacao'),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Setor'),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
