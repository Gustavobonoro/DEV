from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    codigo = models.CharField(max_length=50, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    # Remova a linha 'foto = models.ImageField(...)
    
    def __str__(self):
        return self.nome

class ImagemProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/')
    
    def __str__(self):
        return f"Imagem de {self.produto.nome}"