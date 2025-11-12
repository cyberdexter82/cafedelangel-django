# usuarios/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario # Importa tu modelo de usuario personalizado

# Este es el formulario de CREACIÓN de usuarios
# Usamos 'UserCreationForm' como base
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario  # Le decimos que use tu modelo 'Usuario'
        # Define los campos que aparecerán en el formulario de registro
        # 'username' y los campos de contraseña ('password' y 'password2')
        # ya están incluidos por defecto en UserCreationForm.
        # Puedes añadir más campos aquí si los tienes en tu modelo (ej: 'email')
        fields = ('username', 'email') # <-- Añade 'email' o los campos que quieras

# Este es el formulario para MODIFICAR usuarios (útil para el panel de admin)
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario # Le decimos que use tu modelo 'Usuario'
        fields = UserChangeForm.Meta.fields