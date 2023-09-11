from rest_framework import status
from rest_framework.views import APIView
from .serializers import LoginSerializer
from rest_framework.response import Response
from .models import Cliente, Factura
from .serializers import FacturaSerializer

class LoginView(APIView):
   def post(self, request):
      serializer = LoginSerializer(data=request.data)
      if serializer.is_valid():
         email=serializer.validated_data['email'],
         password=serializer.validated_data['password']
         try:
            client = Cliente.objects.get(email=email[0])
            if client.password != password:
               return Response({'message': 'Bad credentials'}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({ 'id': client.id, 'email': client.email, 'nombre': client.nombre, 'apellido': client.apellido })
         except Cliente.DoesNotExist:
            return Response({'message': 'Cliente  no existe, check your email'}, status=status.HTTP_404_NOT_FOUND)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientFacturasView(APIView):
   def get(self, request, cliente_id):
      try:
         Cliente.objects.get(id=cliente_id)
      except Cliente.DoesNotExist:
         return Response({'message': 'Cliente no existe'}, status=status.HTTP_404_NOT_FOUND)
      
      facturas = Factura.objects.filter(cliente_id=cliente_id)
      serializer = FacturaSerializer(facturas, many=True)
      return Response(serializer.data)