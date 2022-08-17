from django.forms import ModelForm
from .models import Livros, Autor, Emprestimo

class LivrosForm(ModelForm):
    model = Livros
    fields = '__all__'

class AutorForm(ModelForm):
    model = Autor
    fields = '__all__'

class EmprestimoForm(ModelForm):
    model = Emprestimo
    fields = '__all__'