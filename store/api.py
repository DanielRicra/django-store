from store.models import Categoria
from rest_framework import viewsets, permissions
from .serializers import CategoriaSerializer

class CategoryViewSet(viewsets.ModelViewSet):
   queryset = Categoria.objects.all()
   permission_classes = [
      permissions.AllowAny
   ]
   serializer_class = CategoriaSerializer