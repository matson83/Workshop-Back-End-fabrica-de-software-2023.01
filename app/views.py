from django.shortcuts import render
from rest_framework import viewsets
from app.serializer import ClienteSerializer,ProdutoSerializer
from app.models import Cliente,Produto
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer