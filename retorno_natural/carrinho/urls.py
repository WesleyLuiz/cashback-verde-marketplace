from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_carrinho, name='ver_carrinho'),
    path('add/<int:produto_id>/', views.add_carrinho, name='add_carrinho'),
]