from django.db import models

class Cliente(models.Model):
   nombre = models.CharField(max_length=100)
   apellido = models.CharField(max_length=100)
   email = models.EmailField(max_length=200)
   password = models.CharField(max_length=100)
   dni = models.CharField(max_length=8, null=True, unique=True)

class ModoPago(models.Model):
   nombre = models.CharField(max_length=100)
   descripcion = models.TextField()


class Factura(models.Model):
   num_factura = models.AutoField(primary_key=True)
   fecha = models.DateTimeField(auto_now_add=True)
   cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
   modo_pago = models.ForeignKey(ModoPago, on_delete=models.SET_NULL, null=True)

class Categoria(models.Model):
   nombre = models.CharField(max_length=150)
   descripcion = models.TextField()

class Producto(models.Model):
   nombre = models.CharField(max_length=160)
   precio = models.DecimalField(max_digits=8, decimal_places=2)
   stock = models.IntegerField()
   categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)


class Detalle(models.Model):
   factura = models.ForeignKey(Factura, on_delete=models.DO_NOTHING)
   producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
   cantidad = models.IntegerField()
   total = models.DecimalField(max_digits=8, decimal_places=2)

   class Meta:
      unique_together = ('factura', 'producto')

