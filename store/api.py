from store.models import Categoria, Producto, Cliente, Factura, ModoPago, Detalle
from rest_framework import viewsets, permissions
from .serializers import CategoriaSerializer, ProductoSerializer, ClienteSerializer, FacturaSerializer, ModoPagoSerializer, DetalleSerializer

class CategoryViewSet(viewsets.ModelViewSet):
   queryset = Categoria.objects.all()
   permission_classes = [
      permissions.AllowAny
   ]
   serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
   queryset = Producto.objects.all()
   permission_classes = [ permissions.AllowAny ]
   serializer_class = ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
   queryset = Cliente.objects.all()
   permission_classes = [ permissions.AllowAny ]
   serializer_class = ClienteSerializer

class FacturaViewSet(viewsets.ModelViewSet):
   queryset = Factura.objects.all()
   permission_classes = [ permissions.AllowAny]
   serializer_class = FacturaSerializer

class ModoPagoViewSet(viewsets.ModelViewSet):
   queryset = ModoPago.objects.all()
   permission_classes = [ permissions.AllowAny]
   serializer_class = ModoPagoSerializer


class DetalleViewSet(viewsets.ModelViewSet):
   queryset = Detalle.objects.all()
   permission_classes = [ permissions.AllowAny]
   serializer_class = DetalleSerializer