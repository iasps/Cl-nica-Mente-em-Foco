from django.contrib import admin

# Register your models here.

from CMFapp.models import Profissional # "*" imporata nossos models
from CMFapp.models import Atendente

class ProfissionalAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'email') #search_fields: Permite a pesquisa por determinados campos.
    list_filter = ('area_de_atuacao',) #list_filter: Adiciona filtros na barra lateral direita da interface administrativa. No caso, estamos adicionando um filtro pelo campo especialidade.
    list_display = ('nome', 'email', 'area_de_atuacao') #list_display: Define quais campos serão exibidos na lista de objetos no admin.

class AtendenteAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'email')
    list_display = ('nome', 'email') 


admin.site.register(Profissional, ProfissionalAdmin) #adiciona a interface do adm
admin.site.register(Atendente, AtendenteAdmin) #adiciona a interface do adm
