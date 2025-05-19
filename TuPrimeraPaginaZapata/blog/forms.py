from django import forms
from .models import Autor, Categoria, Articulo

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'bio', 'email'] # Campos que quieres en el formulario
        # Personalización opcional de widgets (cómo se ven los campos)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo del autor'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Una breve biografía...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
        }
        labels = { # Etiquetas personalizadas para los campos
            'nombre': 'Nombre del Autor',
            'bio': 'Biografía',
            'email': 'Correo Electrónico',
        }
        help_texts = { # Textos de ayuda opcionales
            'email': 'Asegúrate de que sea un correo único.',
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Tecnología, Viajes, Cocina'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción breve de la categoría (opcional)'}),
        }
        labels = {
            'nombre': 'Nombre de la Categoría',
            'descripcion': 'Descripción',
        }

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        # Excluimos fecha_publicacion porque se manejará automáticamente con `default=timezone.now`
        fields = ['titulo', 'contenido', 'autor', 'categoria', 'imagen_destacada']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título atractivo para tu artículo'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Escribe aquí el contenido de tu artículo...'}),
            'autor': forms.Select(attrs={'class': 'form-select'}), # Para que se vea bien con Bootstrap
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'imagen_destacada': forms.ClearableFileInput(attrs={'class': 'form-control'}), # Permite limpiar la selección de archivo
        }
        labels = {
            'titulo': 'Título del Artículo',
            'contenido': 'Contenido Principal',
            'autor': 'Autor del Artículo',
            'categoria': 'Categoría Principal',
            'imagen_destacada': 'Imagen Destacada (Opcional)',
        }
        help_texts = {
            'categoria': 'Puedes dejarlo en blanco si no aplica.',
        }

# Formulario para buscar artículos (no basado en un modelo directamente)
class BusquedaArticuloForm(forms.Form):
    query = forms.CharField(
        label='Buscar artículo por título',
        max_length=100,
        required=False, # Para permitir búsquedas vacías o que el campo no sea obligatorio
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe palabras clave del título...'})
    )