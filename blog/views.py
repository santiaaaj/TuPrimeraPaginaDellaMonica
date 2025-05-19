from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm
from .models import Post

def index(request):
    return render(request, 'blog/index.html')

def home(request):
    return render(request, 'blog/home.html')

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Autor'})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Categoría'})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Post'})

def buscar_post(request):
    resultados = []
    if request.method == 'POST':
        form = BusquedaPostForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaPostForm()
    return render(request, 'blog/buscar.html', {'form': form, 'resultados': resultados})

