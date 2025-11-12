from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    
    # Usamos DecimalField para evitar errores de redondeo con el dinero
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Precio anterior (para mostrar ofertas), es opcional
    precio_anterior = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # 'upload_to' le dice a Django que guarde las imágenes 
    # en una carpeta llamada 'productos' dentro de tu carpeta 'media'
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    
    # Campo opcional para las estrellas (de 1 a 5)
    estrellas = models.IntegerField(default=5, blank=True, null=True)

    def __str__(self):
        return self.nombre