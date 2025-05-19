from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages # Para mostrar mensajes de éxito/error al usuario
from .models import Autor, Categoria, Articulo
from .forms import AutorForm, CategoriaForm, ArticuloForm, BusquedaArticuloForm

# Vista para la página de inicio (mostrará los últimos artículos)
def home(request):
    # Obtener los últimos 5 artículos ordenados por fecha de publicación descendente
    ultimos_articulos = Articulo.objects.all().order_by('-fecha_publicacion')[:5]
    context = {
        'ultimos_articulos': ultimos_articulos,
        'titulo_pagina': 'Inicio del Blog' # Para el título de la pestaña del navegador
    }
    return render(request, 'blog/home.html', context)

# Vista para listar todos los artículos
def listar_articulos(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    context = {
        'articulos': articulos,
        'titulo_pagina': 'Todos los Artículos'
    }
    return render(request, 'blog/listar_articulos.html', context)

# Vista para mostrar el detalle de un artículo específico
def detalle_articulo(request, pk):
    # get_object_or_404 intentará obtener el artículo con la Primary Key (pk) dada.
    # Si no lo encuentra, automáticamente devolverá una página de error 404 (Not Found).
    articulo = get_object_or_404(Articulo, pk=pk)
    context = {
        'articulo': articulo,
        'titulo_pagina': articulo.titulo # El título de la página será el título del artículo
    }
    return render(request, 'blog/detalle_articulo.html', context)

# --- Vistas para crear instancias de los modelos (usando los formularios) ---

def crear_autor(request):
    if request.method == 'POST': # Si el formulario fue enviado (método POST)
        form = AutorForm(request.POST) # Crea una instancia del formulario con los datos enviados
        if form.is_valid(): # Verifica si los datos son válidos
            form.save() # Guarda el nuevo autor en la base de datos
            messages.success(request, '¡Autor creado exitosamente!') # Mensaje de éxito
            return redirect('home') # Redirige a la página de inicio (o a donde quieras)
    else: # Si es una solicitud GET (primera vez que se accede a la página)
        form = AutorForm() # Crea una instancia vacía del formulario
    
    context = {
        'form': form,
        'titulo_pagina': 'Crear Nuevo Autor',
        'tipo_entidad': 'Autor' # Para usar en la plantilla del formulario genérico
    }
    return render(request, 'blog/formulario_generico.html', context)

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Categoría creada exitosamente!')
            return redirect('home')
    else:
        form = CategoriaForm()
        
    context = {
        'form': form,
        'titulo_pagina': 'Crear Nueva Categoría',
        'tipo_entidad': 'Categoría'
    }
    return render(request, 'blog/formulario_generico.html', context)

def crear_articulo(request):
    if request.method == 'POST':
        # request.FILES es necesario para manejar la subida de archivos (como la imagen_destacada)
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Artículo creado y publicado exitosamente!')
            # Es común redirigir a la lista de artículos o al detalle del artículo recién creado
            return redirect('listar_articulos')
    else:
        form = ArticuloForm()
        
    context = {
        'form': form,
        'titulo_pagina': 'Crear Nuevo Artículo',
        'tipo_entidad': 'Artículo',
        'enctype_multipart': True # Necesario en la plantilla para que el form permita subida de archivos
    }
    return render(request, 'blog/formulario_generico.html', context)

# --- Vista para buscar artículos ---
def buscar_articulos(request):
    # Instancia el formulario. Si hay datos GET (porque se envió el formulario), los usa.
    form = BusquedaArticuloForm(request.GET or None)
    resultados = [] # Lista para guardar los artículos encontrados
    query = "" # Para guardar el término de búsqueda

    if form.is_valid(): # Valida el formulario (aunque aquí es simple, es buena práctica)
        query = form.cleaned_data.get('query') # Obtiene el valor del campo 'query'
        if query: # Si el usuario ingresó algo para buscar
            # __icontains realiza una búsqueda que no distingue mayúsculas/minúsculas
            # y busca si el 'query' está contenido en el 'titulo'.
            resultados = Articulo.objects.filter(titulo__icontains=query).order_by('-fecha_publicacion')
            if not resultados.exists():
                messages.info(request, f'No se encontraron artículos que contengan "{query}" en el título.')
        # else:
            # Si query está vacío pero el formulario es válido (porque query no es required)
            # podrías mostrar todos los artículos o un mensaje.
            # Por ahora, si no hay query, resultados quedará vacío.

    context = {
        'form': form,
        'query': query, # Pasamos la query para mostrarla en la plantilla si hubo búsqueda
        'resultados': resultados,
        'titulo_pagina': 'Buscar Artículos'
    }
    return render(request, 'blog/buscar_articulos.html', context)