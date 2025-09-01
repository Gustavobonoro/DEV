from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_view, name='catalogo'),
    path('produto/<int:produto_id>/', views.produto_detalhe_view, name='produto_detalhe'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('contato/', views.contato_view, name='contato'),
]