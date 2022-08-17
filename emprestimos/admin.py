from django.contrib import admin
from .models import Livros, Autor, Emprestimo
from .forms import LivrosForm, AutorForm, EmprestimoForm

# Register your models here.
class LivrosAdminStackedInline(admin.StackedInline):
    model = Livros
    form = LivrosForm
    search_fields = ['nome', 'livros__nome']
    extra = 1

class AutorAdminStackedInline(admin.StackedInline):
    model = Autor
    form = AutorForm
    list_display = ('nome', 'data_de_cadastro', 'email')
    search_fields = ['nome', 'data_de_cadastro', 'email']

class EmprestimoAdminStackedInline(admin.StackedInline):
    model = Emprestimo
    form = EmprestimoForm
    autocomplete_fields = ['emprestimo']
    extra = 1
    readonly_fields=('valor_total',)


admin.site.register(Livros, LivrosAdminStackedInline)
admin.site.register(Autor, AutorAdminStackedInline)
admin.site.register(Emprestimo, EmprestimoAdminStackedInline)