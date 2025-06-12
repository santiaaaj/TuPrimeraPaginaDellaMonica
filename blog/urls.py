from django.urls import path
from . import views
#from .views import about_view, pages_list, PageCreateView, PageDeleteView, PageUpdateView, registro
from .views import registro, about_view, perfil_view

urlpatterns = [
    path('', views.home, name='home'),
    path('autor/', views.crear_autor, name='crear_autor'),
    path('categoria/', views.crear_categoria, name='crear_categoria'),
    path('post/', views.crear_post, name='crear_post'),
    path('buscar/', views.buscar_post, name='buscar_post'),
    path('about/', about_view, name='about'),
    path('pages/', views.pages_list, name='pages_list'),
    path('pages/<int:page_id>/', views.page_details, name='page_detail'),
    #path('pages/create/', PageCreateView.as_view(), name='page_create'),
    #path('pages/<int:pk>/edit/', PageUpdateView.as_view(), name='page_edit'),
    #path('pages/<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),
    path("registro/", registro, name="registro"),
    path('perfil/', perfil_view, name='perfil'),
]
