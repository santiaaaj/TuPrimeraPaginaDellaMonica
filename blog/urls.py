from django.urls import path
from . import views
from .views import registro, about_view, perfil_view
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('autor/', views.crear_autor, name='crear_autor'),
    path('categoria/', views.crear_categoria, name='crear_categoria'),
    path('post/', views.crear_post, name='crear_post'),
    path('buscar/', views.buscar_post, name='buscar_post'),
    path('about/', about_view, name='about'),
    path('pages/', views.pages_list, name='pages_list'),
    path('pages/<int:page_id>/', views.page_details, name='page_detail'),
    path("registro/", registro, name="registro"),
    path('perfil/', perfil_view, name='perfil'),
    path('profile/change_password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name='change_password'),
    path('profile/change_password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/change_password_done.html'), name='password_change_done'),
]
