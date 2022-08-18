from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Livros, Autor, Emprestimo
# Create your views here.

class LivrosListView(ListView):
    model = Livros
    context_object_name = 'livros'
    template_name = 'livros/listar.html'
    
class LivrosDetailView(DetailView):
    model = Livros
    context_object_name = 'livros'
    template_name = 'livros/detalhe.html'

