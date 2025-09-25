from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Produto, Categoria, ImagemProduto, Banner

def catalogo_view(request):
    categorias = Categoria.objects.all()
    banners = Banner.objects.all()
    contexto = {
        'categorias': categorias,
        'banners': banners
    }
    return render(request, 'catalogo/catalogo.html', contexto)

def catalogo_filtrado_view(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    produtos = Produto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()
    banners = Banner.objects.all()
    contexto = {
        'categoria_selecionada': categoria,
        'produtos': produtos,
        'categorias': categorias,
        'banners': banners
    }
    return render(request, 'catalogo/catalogo.html', contexto)

def produto_detalhe_view(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    imagens = ImagemProduto.objects.filter(produto=produto)
    categorias = Categoria.objects.all()
    contexto = {
        'produto': produto,
        'imagens': imagens,
        'categorias': categorias
    }
    return render(request, 'catalogo/produto_detalhe.html', contexto)

def sobre_view(request):
    categorias = Categoria.objects.all()
    contexto = {'categorias': categorias}
    return render(request, 'catalogo/sobre.html', contexto)

def contato_view(request):
    categorias = Categoria.objects.all()
    contexto = {'categorias': categorias}
    return render(request, 'catalogo/contato.html', contexto)

def search_products(request):
    query = request.GET.get('q', '')
    if len(query) > 2:
        produtos = Produto.objects.filter(nome__icontains=query) | \
                   Produto.objects.filter(descricao__icontains=query)
        
        results = []
        for produto in produtos:
            results.append({
                'nome': produto.nome,
                'url': f'/catalogo/produto/{produto.id}/',
                'imagem_url': produto.imagemproduto_set.first().imagem.url if produto.imagemproduto_set.exists() else ''
            })
        return JsonResponse(results, safe=False)
    
    return JsonResponse([], safe=False)