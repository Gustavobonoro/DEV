from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_view, name='catalogo'),
    path('categoria/<int:categoria_id>/', views.catalogo_filtrado_view, name='catalogo_filtrado'),
    path('produto/<int:produto_id>/', views.produto_detalhe_view, name='produto_detalhe'),
    path('search/', views.search_products, name='search'), # **NOVA URL**
    path('sobre/', views.sobre_view, name='sobre'),
    path('contato/', views.contato_view, name='contato'),
]