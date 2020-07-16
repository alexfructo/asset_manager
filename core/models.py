from django.db import models
from django.contrib.auth.models import User

class Localizacao(models.Model):
    codigo = models.AutoField(primary_key=True)
    criado_em = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering = ["nome"]
        verbose_name = 'localização'
        verbose_name_plural = 'localizações'

    def __str__(self):
        return self.nome

class Setor(models.Model):
    codigo = models.AutoField(primary_key=True)
    criado_em = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering = ["nome"]
        verbose_name = 'setor'
        verbose_name_plural = 'setores'

    def __str__(self):
        return self.nome

class Grupo(models.Model):
    codigo = models.AutoField(primary_key=True)
    criado_em = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering = ["nome"]
        verbose_name = 'grupo'
        verbose_name_plural = 'grupos'

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    codigo = models.AutoField(primary_key=True)
    criado_em = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering = ["nome"]
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome

class Fabricante(models.Model):
    codigo = models.AutoField(primary_key=True)
    criado_em = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering = ["nome"]
        verbose_name = 'fabricante'
        verbose_name_plural = 'fabricantes'

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    codigo = models.AutoField(primary_key=True)
    criado_em = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    localizacao = models.ForeignKey('Localizacao', on_delete=models.PROTECT, null=True, blank=True)
    setor = models.ForeignKey('Setor', on_delete=models.PROTECT, null=True, blank=True)
    grupo = models.ForeignKey('Grupo', on_delete=models.PROTECT, null=True, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT, null=True, blank=True)
    fabricante = models.ForeignKey('Fabricante', on_delete=models.PROTECT, null=True, blank=True)
    modelo = models.CharField(max_length=100, null=True, blank=True)
    numero_serie = models.CharField(max_length=32, null=True, blank=True)
    numero_patrimonio = models.CharField(max_length=32, null=True, blank=True)
    status_opcoes = [
        (0, 'Armazenado'),
        (1, 'Alocado'),
        (2, 'Descartado'),
    ]
    status = models.IntegerField(choices=status_opcoes, default=0, blank=False, null=False)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["codigo", "categoria", "fabricante"]
        verbose_name = 'equipamento'
        verbose_name_plural = 'equipamentos'

    def listar_json(self):
        return {
            'codigo' : self.codigo,
            'criado_em' : self.criado_em,
            'modificado_em' : self.modificado_em,
            'usuario' : self.usuario.__str__(),
            'localizacao' : self.localizacao.__str__(),
            'setor' : self.setor.__str__(),
            'grupo' : self.grupo.__str__(),
            'categoria' : self.categoria.__str__(),
            'fabricante' : self.fabricante.__str__(),
            'modelo' : self.modelo,
            'numero_serie' : self.numero_serie,
            'numero_patrimonio' : self.numero_patrimonio,
            'status' : self.get_status_display(),
            'observacoes' : self.observacoes
        }
