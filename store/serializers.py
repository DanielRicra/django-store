from rest_framework import serializers
from .models import Categoria, Producto, Cliente, Factura, ModoPago, Detalle

class CategoriaSerializer(serializers.ModelSerializer):
   class Meta:
      model = Categoria
      fields = ['id', 'nombre', 'descripcion']


class ProductoSerializer(serializers.ModelSerializer):
   class Meta:
      model = Producto
      fields = '__all__'

   def to_representation(self, instance):
      rep = super().to_representation(instance)
      rep['categoria'] = CategoriaSerializer(instance.categoria).data
      return rep


class ClienteSerializer(serializers.ModelSerializer):
   class Meta:
      model = Cliente
      fields = '__all__'


class ModoPagoSerializer(serializers.ModelSerializer):
   class Meta:
      model = ModoPago
      fields = '__all__'


class DetalleSerializer(serializers.ModelSerializer):
   class Meta:
      model = Detalle
      fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
   productos = ProductoSerializer(many=True, read_only=True)
   class Meta:
      model = Factura
      fields = ['num_factura', 'fecha', 'cliente', 'modo_pago', 'productos']


class LoginSerializer(serializers.Serializer):
   email = serializers.CharField()
   password = serializers.CharField()