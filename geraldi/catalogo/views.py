from django.shortcuts import render, get_object_or_404
from .models import Produto, Categoria, ImagemProduto  # Importe o novo modelo

def catalogo_view(request):
    # Pega todas as categorias do banco de dados
    categorias = Categoria.objects.all()

    # Cria um dicionário para enviar as categorias e seus produtos para o template
    contexto = {
        'categorias': categorias
    }

    # Renderiza o template HTML e passa os dados para ele
    return render(request, 'catalogo/catalogo.html', contexto)

def produto_detalhe_view(request, produto_id):
    # Pega um produto específico por seu ID, ou retorna erro 404 se não existir
    produto = get_object_or_404(Produto, pk=produto_id)
    
    # Pega todas as imagens relacionadas a este produto
    imagens = ImagemProduto.objects.filter(produto=produto)

    # Cria o dicionário com os dados do produto e suas imagens
    contexto = {
        'produto': produto,
        'imagens': imagens
    }
    
    # Renderiza o novo template de detalhes do produto
    return render(request, 'catalogo/produto_detalhe.html', contexto)
def sobre_view(request):
    return render(request, 'catalogo/sobre.html')

def contato_view(request):
    return render(request, 'catalogo/contato.html')