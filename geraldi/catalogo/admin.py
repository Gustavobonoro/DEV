from django.contrib import admin
from .models import Categoria, Produto, ImagemProduto, Banner # Importe o novo modelo

# Esta classe cria uma interface para adicionar imagens
# diretamente na página de cada produto no admin
class ImagemProdutoInline(admin.TabularInline):
    model = ImagemProduto
    extra = 1 # Define quantos formulários vazios de imagem aparecem por padrão

class ProdutoAdmin(admin.ModelAdmin):
    # A linha abaixo diz ao Django para incluir a interface de imagens
    # na página de edição do produto
    inlines = [ImagemProdutoInline]
    
    # Esta linha mostra as colunas que você quer ver na lista de produtos
    list_display = ('nome', 'categoria', 'preco', 'codigo')

admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Banner) # **Esta linha é crucial**