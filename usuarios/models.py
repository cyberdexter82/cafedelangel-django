# usuarios/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Creamos un modelo de Usuario que "hereda" todo lo de Django
# (username, password, email, etc.)
class Usuario(AbstractUser):
    # Puedes añadir campos extra aquí si quisieras, por ejemplo:
    # fecha_nacimiento = models.DateField(null=True, blank=True)
    
    # Dejándolo así, usará los campos por defecto de Django
    pass