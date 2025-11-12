from django.db import models
from django.conf import settings # Importamos settings para referenciar AUTH_USER_MODEL

# Modelo Producto (Existente)
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


# ----------------------------------------------------------------------
# 🌟 MODELO NUEVO 1: Perfil de Usuario (Para el Avatar)
# ----------------------------------------------------------------------
class Profile(models.Model):
    # Relación uno a uno con el modelo de usuario (usando AUTH_USER_MODEL)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Campo para la imagen de perfil (avatar)
    # Se guardará en media/avatars/
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'


# ----------------------------------------------------------------------
# 🌟 MODELO NUEVO 2: Reseña (Review)
# ----------------------------------------------------------------------
class Review(models.Model):
    # Opciones de calificación (de 1 a 5 estrellas)
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    
    # Relación con el usuario que creó la reseña
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Calificación (Rating)
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    
    # Texto del comentario
    comment = models.TextField()
    
    # Imagen opcional que el usuario puede subir con la reseña
    image = models.ImageField(upload_to='review_images/', blank=True, null=True)
    
    # Fecha de creación (se establece automáticamente)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reseña de {self.user.username} ({self.rating} estrellas)'
    
    class Meta:
        # Ordena las reseñas para que las más recientes aparezcan primero
        ordering = ['-created_at']