from rest_framework import routers
from django.urls import path
from .views import LoginView
from .api import CategoryViewSet, ProductoViewSet, ClienteViewSet, FacturaViewSet, ModoPagoViewSet, DetalleViewSet

router = routers.DefaultRouter()

router.register('api/categorias', CategoryViewSet, 'categorias')
router.register('api/productos', ProductoViewSet, 'productos')
router.register('api/clientes', ClienteViewSet, 'clientes')
router.register('api/facturas', FacturaViewSet, 'facturas')
router.register('api/modopagos', ModoPagoViewSet, 'modopagos')
router.register('api/detalles', DetalleViewSet, 'detalles')

urlpatterns = [
   *router.urls,
   path('api/login/', LoginView.as_view(), name='login'),
]