from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrinho, ItemCarrinho
from core.models import Produto
from django.contrib import messages

def add_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)

    item, created = ItemCarrinho.objects.get_or_create(
        carrinho=carrinho,
        produto=produto
    )

    if not created:
        item.quantidade += 1
        item.save()

    messages.success(request, f"{produto.nome} adicionado ao carrinho!")

    # 👇 pega o "next"
    next_url = request.GET.get('next')

    if next_url:
        return redirect(next_url)

    return redirect('ver_carrinho')


# 👇 mostra o carrinho
def ver_carrinho(request):
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
    itens = ItemCarrinho.objects.filter(carrinho=carrinho)

    total = sum(item.produto.preco * item.quantidade for item in itens)

    return render(request, 'carrinho/carrinho.html', {
        'itens': itens,
        'total': total
    })