from django import forms
from .models import Autor, Categoria, Post, Perfil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class BusquedaPostForm(forms.Form):
    titulo = forms.CharField(label="Buscar por título", max_length=100)

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]    


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['bio', 'avatar']        
