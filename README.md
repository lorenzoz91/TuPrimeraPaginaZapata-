# TuPrimeraPaginaZapata (Blog con Django)

Proyecto de un blog simple desarrollado con Django, aplicando el patrón Modelo-Vista-Plantilla (MVT). Cumple con los requisitos de herencia de plantillas HTML, un modelo de base de datos con tres clases (Autor, Categoria, Articulo), formularios para la inserción de datos en cada una de estas clases y un formulario para la búsqueda de artículos en la base de datos.

## Requisitos Previos

* Python 3.8+
* Django (versión utilizada: la especificada en `requirements.txt` o la última estable al momento de la creación)
* pip (manejador de paquetes de Python)

## Configuración del Entorno Local

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/lorenzoz91/TuPrimeraPaginaZapata.git](https://github.com/lorenzoz91/TuPrimeraPaginaZapata.git)
    cd TuPrimeraPaginaZapata
    ```

2.  **(Recomendado) Crear y activar un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows:
    # venv\Scripts\activate
    # En macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    (Si se incluye un archivo `requirements.txt`, usar el segundo comando).
    ```bash
    pip install django
    # O, si existe requirements.txt:
    # pip install -r requirements.txt
    ```

4.  **Realizar migraciones para crear la base de datos:**
    ```bash
    python manage.py migrate
    ```

5.  **Crear un superusuario para acceder al panel de administración:**
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones en pantalla (nombre de usuario, correo opcional, contraseña).

6.  **Ejecutar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    El sitio estará disponible en `http://127.0.0.1:8000/`.

## Orden de Prueba y Ubicación de Funcionalidades

Una vez que el servidor esté corriendo, las funcionalidades se pueden probar de la siguiente manera:

1.  **Página de Inicio:**
    * **URL:** `http://127.0.0.1:8000/`
    * **Descripción:** Página principal que muestra un mensaje de bienvenida y los artículos más recientes. Permite la navegación a otras secciones.

2.  **Panel de Administración (Gestión de Datos):**
    * **URL:** `http://127.0.0.1:8000/admin/`
    * **Descripción:** Interfaz para la administración directa de Autores, Categorías y Artículos. Se accede con las credenciales del superusuario. El enlace "Admin Panel" en la barra de navegación también dirige aquí si el usuario está autenticado como superusuario.
    * **Prueba Sugerida:** Se recomienda crear al menos un Autor y una Categoría desde esta interfaz para tener datos disponibles para los formularios del sitio.

3.  **Crear Nuevo Autor:**
    * **URL:** `http://127.0.0.1:8000/autor/nuevo/` (Accesible desde el menú "Crear Nuevo" > "Autor")
    * **Descripción:** Formulario para registrar nuevos autores en el sistema.

4.  **Crear Nueva Categoría:**
    * **URL:** `http://127.0.0.1:8000/categoria/nueva/` (Accesible desde el menú "Crear Nuevo" > "Categoría")
    * **Descripción:** Formulario para crear categorías que permitan organizar los artículos.

5.  **Crear Nuevo Artículo:**
    * **URL:** `http://127.0.0.1:8000/articulo/nuevo/` (Accesible desde el menú "Crear Nuevo" > "Artículo")
    * **Descripción:** Formulario para la publicación de nuevos artículos. Requiere seleccionar un autor y una categoría existentes, y permite la subida de una imagen destacada.

6.  **Ver Todos los Artículos:**
    * **URL:** `http://127.0.0.1:8000/articulos/` (Accesible desde el menú "Artículos")
    * **Descripción:** Muestra una lista paginada de todos los artículos publicados, con un breve extracto, autor, categoría e imagen.

7.  **Ver Detalle de un Artículo:**
    * **Acceso:** Haciendo clic en el título de un artículo o en el enlace "Leer más" desde la página de inicio o la lista de artículos.
    * **URL Ejemplo:** `http://127.0.0.1:8000/articulo/ID_DEL_ARTICULO/` (donde `ID_DEL_ARTICULO` es el identificador numérico del artículo).
    * **Descripción:** Presenta el contenido completo de un artículo seleccionado, incluyendo su imagen destacada y metadatos.

8.  **Buscar Artículos:**
    * **URL:** `http://127.0.0.1:8000/buscar/` (Accesible desde el menú "Buscar")
    * **Descripción:** Permite a los usuarios buscar artículos por palabras clave presentes en el título. Los resultados se muestran en la misma página, o un mensaje si no se encuentran coincidencias.

## Estructura del Proyecto (Patrón MVT)

* **Modelos (`blog/models.py`):**
    * `Autor`: Define la estructura para los datos de los autores de los artículos.
    * `Categoria`: Define la estructura para las categorías de los artículos.
    * `Articulo`: Define la estructura para cada artículo del blog, incluyendo título, contenido, autor, categoría, fecha de publicación e imagen destacada.
* **Vistas (`blog/views.py`):** Implementan la lógica de negocio. Gestionan las solicitudes HTTP, interactúan con los modelos para obtener o guardar datos, y seleccionan la plantilla adecuada para renderizar la respuesta.
* **Plantillas (`blog/templates/blog/`):** Son archivos HTML que definen la interfaz de usuario. Se utiliza el sistema de plantillas de Django, incluyendo la herencia desde una plantilla base (`base.html`) para mantener una estructura y diseño consistentes. Se incluyen plantillas para la página de inicio, listado de artículos, detalle de artículo, formularios de creación y la página de búsqueda.
* **Formularios (`blog/forms.py`):**
    * Se emplean `ModelForm` para facilitar la creación y validación de datos para los modelos `Autor`, `Categoria` y `Articulo`.
    * Un `Form` estándar se utiliza para el formulario de búsqueda de artículos.
* **URLs (`TuPrimeraPaginaZapata/urls.py` y `blog/urls.py`):** Definen el mapeo entre las URLs y las vistas correspondientes, permitiendo el enrutamiento de las solicitudes.

## Autor del Proyecto

* lorenzoz91