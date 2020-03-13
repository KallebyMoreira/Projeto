from django.contrib import admin
from .models import Noticia,Pessoa,Tag,Comentario,Categoria,Foto

@admin.register(Noticia,Pessoa,Tag,Categoria,Comentario,Foto)
class NoticiaAdmin(admin.ModelAdmin):
    pass