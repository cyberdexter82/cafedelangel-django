from django.contrib import admin
from .models import Producto  # Importamos tu nuevo modelo

# Register your models here.

# Esto registra el modelo 'Producto' en el panel de admin
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'estrellas')
    search_fields = ('nombre',)
