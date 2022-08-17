from django.db import models

# Create your models here.
class Livros(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField('Descrição', max_length=255)
    editora = models.CharField(max_length=200)
    quantidade = models.IntegerField('Quantidade')
    data_de_cadastro = models.DateTimeField('Data de cadastro')
    autor = models.CharField(max_length=150)

class Autor(models.Model):
    nome = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    data_de_cadastro = models.DateTimeField('Data de cadastro')

class Emprestimo(models.Model):
    quantidade = models.IntegerField('Quantidade')
    nome = models.CharField(max_length=40)
    autor = models.CharField(max_length=150)