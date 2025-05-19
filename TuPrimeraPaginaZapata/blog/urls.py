from django.urls import path
from . import views # Importa las vistas de la aplicación blog

# app_name = 'blog' # Opcional: para namespacing de URLs si tienes muchas apps

urlpatterns = [
    # URL para la página de inicio del blog (que definimos en views.home)
    path('', views.home, name='home'),

    # URL para listar todos los artículos
    path('articulos/', views.listar_articulos, name='listar_articulos'),

    # URL para ver el detalle de un artículo específico
    # <int:pk> captura un entero de la URL y lo pasa como argumento 'pk' a la vista
    path('articulo/<int:pk>/', views.detalle_articulo, name='detalle_articulo'),

    # URLs para crear nuevas entidades
    path('autor/nuevo/', views.crear_autor, name='crear_autor'),
    path('categoria/nueva/', views.crear_categoria, name='crear_categoria'),
    path('articulo/nuevo/', views.crear_articulo, name='crear_articulo'),

    # URL para la página de búsqueda de artículos
    path('buscar/', views.buscar_articulos, name='buscar_articulos'),
]