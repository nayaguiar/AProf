from django.contrib import admin

# default: "Administração do Django"
admin.site.site_header= 'Painel de Controle'

# default: "Administração do Site"
admin.site.index_title = 'Recursos'

# default: ”Site de administração do Django"
admin.site.site_title = 'Título HTML do Site'

# Register your models here.
from .models import Curso
from .models import Turma
from .models import Professor

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria', 'ementa', 'valor')

admin.site.register(Curso, CursoAdmin)

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('data_inicio', 'data_termino', 'hora_inicio', 'hora_termino')

admin.site.register(Turma, TurmaAdmin)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'valor_hora_aula')

admin.site.register(Professor, ProfessorAdmin)


