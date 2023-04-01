from rest_framework import serializers

from app.models import Cliente,Produto

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','nome','cpf','email','contato']

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','nome','quantidade']

