from django.urls import path
from . import views

urlpatterns = [

    # ================================
    # 🔵 PÁGINA PRINCIPAL
    # ================================
    path('', views.pagina_practica_view, name='pagina_practica'),

    # ================================
    # 🔵 AUTENTICACIÓN
    # ================================
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),  # 🔥 FUNCIONA SIN 405

    # ================================
    # 🔵 FUNCIONALIDAD INTERNA
    # ================================
    path('dejar-resena/', views.dejar_resena, name='dejar_resena'),
    path('subir-avatar/', views.subir_avatar, name='subir_avatar'),

    # ================================
    # 🔵 PÁGINAS INTERNAS
    # ================================
    path('buscador/', views.buscador_view, name='buscador'),
    path('marketing/', views.pagina_practica_view, name='pagina_practica'),
    path('otra_pagina/', views.otra_pagina_view, name='otra_pagina'),
    path('comprar/', views.compra_view, name='comprar'),
    path('resenas/', views.resenas_view, name='resenas'),
    path('acerca/', views.acerca_view, name='acerca'),
    path('autores/', views.autores_view, name='autores'),
    path('producto/', views.detalle_producto_view, name='detalle_producto'),
    path('perfil/', views.profile_view, name='perfil'),
]
