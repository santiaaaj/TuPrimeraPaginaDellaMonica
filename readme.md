
# Tu Primera Página Web con Django (Blog Personal)

Este es un proyecto de desarrollo web construido con Django, que funciona como un blog personal o una plataforma de publicaciones. Permite a los usuarios crear, ver, editar y eliminar publicaciones (posts), así como gestionar autores y categorías. También incluye funcionalidades de autenticación (registro, inicio y cierre de sesión) y perfiles de usuario.

---

## 🚀 Características Principales

* **Gestión de Posts:**
    * Crear, leer, actualizar y eliminar posts.
    * Posts con título, subtítulo, contenido (soporte para Rich Text a través de CKEditor si está configurado), fecha de publicación, imagen, autor y categoría.
* **Gestión de Autores:** Crear y listar autores.
* **Gestión de Categorías:** Crear y listar categorías para organizar los posts.
* **Páginas Estáticas/Información:** Sección de "Páginas" adicional para contenido que no es un post de blog (ej. "Acerca de Mí").
* **Buscador de Posts:** Funcionalidad para buscar posts por título.
* **Autenticación de Usuarios:**
    * Registro de nuevos usuarios.
    * Inicio de sesión.
    * Cierre de sesión.
* **Perfiles de Usuario:**
    * Creación y gestión de perfiles de usuario (con biografía y avatar).
* **Interfaz de Administración Django:** Gestión completa de todos los modelos (Posts, Autores, Categorías, Páginas, Perfiles, Usuarios) a través del panel de administración integrado de Django.
* **Estilos:** Implementación de CSS personalizado para una estética específica.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:**
    * Python 3.x
    * Django 5.2.1
* **Frontend:**
    * HTML5
    * CSS3
    * JavaScript (base)
* **Base de Datos:** SQLite (por defecto en desarrollo, configurable para producción)
* **Manejo de Contenido Enriquecido:** CKEditor (campo `RichTextField` para `Page.contenido` en `blog/models.py`)
* **Manejo de Archivos:** Configuración para servir archivos estáticos (`STATIC_ROOT`, `STATIC_URL`) y archivos media (`MEDIA_ROOT`, `MEDIA_URL`) en desarrollo.

---

## ⚙️ Configuración y Ejecución del Proyecto

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### 1. Clonar el Repositorio (Si aplica)

Si este es un repositorio Git, clónalo:

```bash
git clone <URL_DEL_REPOSITORIO>
cd TuPrimeraPaginaDellaMonica 