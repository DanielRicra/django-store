from rest_framework import routers
from .api import CategoryViewSet

router = routers.DefaultRouter()

router.register('api/categorias', CategoryViewSet, 'categorias')

urlpatterns = router.urls