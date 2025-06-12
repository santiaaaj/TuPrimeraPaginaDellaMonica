from django.shortcuts import render, redirect, get_object_or_404
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm, RegistroUsuarioForm, PerfilForm
from .models import Post, Page, Perfil
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'blog/index.html')

def home(request):
    return render(request, 'blog/home.html')

@login_required
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = AutorForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Autor'})

@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = CategoriaForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Categoría'})

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = PostForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Post'})

@login_required
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

def about_view(request):
    return render(request, 'blog/about.html')

def pages_list(request):
    pages = Page.objects.all()
    return render(request, 'blog/pages_list.html', {'pages': pages})

def page_details(request, page_id):
    post = get_object_or_404(Post, id=page_id)
    return render(request, 'blog/page_detail.html', {'post': post})

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = 'blog/page_form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    success_url = reverse_lazy('pages')

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    template_name = 'blog/page_form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    success_url = reverse_lazy('pages')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'blog/page_confirm_delete.html'
    success_url = reverse_lazy('pages')   

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente
            return redirect("home")
    else:
        form = RegistroUsuarioForm()
    return render(request, "blog/registro.html", {"form": form})     

@login_required
def perfil_view(request):
    Profile, _ = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'blog/perfil.html', {'perfil': Profile})


@login_required
def perfil_view(request):
    perfil_obj, _ = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil_obj)
        if 'avatar-clear' in request.POST:
            perfil_obj.avatar.delete(save=False)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil_obj)

    return render(request, 'blog/perfil.html', {'form': form, 'perfil': perfil_obj})
