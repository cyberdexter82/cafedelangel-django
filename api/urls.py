from django.urls import path
from . import views  # Importa todas las vistas que creamos en api/views.py

urlpatterns = [
    # Este es el "mapa" que conecta las URLs con las vistas (funciones)
    
    # --- Rutas de Autenticación ---
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),

    # ------------------------------------------------
    # 🌟 NUEVAS RUTAS DE FUNCIONALIDAD (Reseñas y Avatar)
    # ------------------------------------------------
    
    # Procesa el formulario de reseña que está en resenas.html (POST)
    path('dejar-resena/', views.dejar_resena, name='dejar_resena'),
    
    # Procesa la subida o actualización del avatar (POST)
    path('subir-avatar/', views.subir_avatar, name='subir_avatar'),
    
    # ------------------------------------------------
    # --- Rutas de la App (existentes) ---
    # ------------------------------------------------
    path('buscador/', views.buscador_view, name='buscador'),
    path('marketing/', views.pagina_practica_view, name='pagina_practica'),
    path('otra_pagina/', views.otra_pagina_view, name='otra_pagina'),
    path('comprar/', views.compra_view, name='comprar'),
    path('resenas/', views.resenas_view, name='resenas'), # Esta vista también mostrará el formulario ahora
    path('acerca/', views.acerca_view, name='acerca'),
    path('autores/', views.autores_view, name='autores'),
    path('producto/', views.detalle_producto_view, name='detalle_producto'),
]