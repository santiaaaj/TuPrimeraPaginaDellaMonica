# TuPrimeraPaginaDellaMonica

Este es mi primer proyecto web con Django, creado como parte de la entrega práctica para desarrollar una aplicación estilo blog. Incluye herencia de plantillas, tres modelos interrelacionados, formularios para insertar datos y un buscador.

---

##  Tecnologías utilizadas

- Python 3.13
- Django 5.x
- HTML + CSS (con uso de `static`)
- SQLite (por defecto en Django)

---

##  Estructura del Proyecto

- **Modelos (`models.py`)**:  
  - `Autor`: nombre, email.  
  - `Categoria`: nombre.  
  - `Post`: título, contenido, fecha, autor, categoría.

- **Formularios (`forms.py`)**:  
  - Un formulario para crear cada modelo.

- **Vistas (`views.py`)**:  
  - `home`: página de inicio.  
  - `crear_autor`: formulario para agregar un autor.  
  - `crear_categoria`: formulario para agregar una categoría.  
  - `crear_post`: formulario para crear una entrada de blog.  
  - `buscar_post`: búsqueda de posts por título.

- **Herencia de plantillas (`templates/`)**:  
  - `base.html`: plantilla base con header e imagen.  
  - Otras plantillas heredan de esta base.

- **Archivos estáticos (`static/`)**:  
  - Imágenes, estilos (`estilos.css`), etc.

---

##  Cómo probar el proyecto

1. **Cloná el repositorio**  
   ```bash
   git clone https://github.com/tuusuario/TuPrimeraPaginaDellaMonica.git
   cd TuPrimeraPaginaDellaMonica
