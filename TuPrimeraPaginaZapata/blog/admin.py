from django.contrib import admin
from .models import Autor, Categoria, Articulo 

@admin.register(Autor) 
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email') 
    search_fields = ('nombre', 'email') 

@admin.register(Categoria) # Registra el modelo Categoria
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',) # Campos a mostrar en la lista de categorías
    search_fields = ('nombre',) # Campo de búsqueda

@admin.register(Articulo) 
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'fecha_publicacion') 
    list_filter = ('fecha_publicacion', 'categoria', 'autor') 
    search_fields = ('titulo', 'contenido') 
    date_hierarchy = 'fecha_publicacion' 

