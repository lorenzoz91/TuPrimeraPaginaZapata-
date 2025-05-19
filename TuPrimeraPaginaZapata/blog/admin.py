from django.contrib import admin
from .models import Autor, Categoria, Articulo # Importa tus modelos

# Opción 1: Con personalización usando decoradores y clases ModelAdmin
# Esta es la forma recomendada para tener más control sobre cómo se ve y funciona el admin.

@admin.register(Autor) # Registra el modelo Autor con su clase de administración personalizada
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email') # Campos que se mostrarán en la lista de autores
    search_fields = ('nombre', 'email') # Campos por los que se podrá buscar

@admin.register(Categoria) # Registra el modelo Categoria
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',) # Campos a mostrar en la lista de categorías
    search_fields = ('nombre',) # Campo de búsqueda

@admin.register(Articulo) # Registra el modelo Articulo
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'fecha_publicacion') # Campos a mostrar
    list_filter = ('fecha_publicacion', 'categoria', 'autor') # Filtros que aparecerán en la barra lateral derecha
    search_fields = ('titulo', 'contenido') # Campos de búsqueda
    date_hierarchy = 'fecha_publicacion' # Añade una navegación jerárquica por fechas sobre la lista
    # Opcional: para campos de autocompletado si tienes muchas instancias de autor o categoria
    # autocomplete_fields = ['autor', 'categoria']

# Opción 2: La forma más simple de registrar los modelos (sin personalización)
# Si la Opción 1 te parece complicada por ahora, puedes usar esta.
# Simplemente comenta o borra las clases AutorAdmin, CategoriaAdmin, ArticuloAdmin y los decoradores @admin.register,
# y descomenta las siguientes tres líneas:

# admin.site.register(Autor)
# admin.site.register(Categoria)
# admin.site.register(Articulo)