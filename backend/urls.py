from django.contrib import admin
from django.urls import path, include, re_path
from api import views as api_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', api_views.login_view, name='inicio'),
]

# -------------------------------------------------------------
# CORRECCIÓN PARA AZURE
# -------------------------------------------------------------
# 1. Configuramos las rutas de archivos estáticos y media
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 2. EL TRUCO: Forzamos a Django a servir las imágenes de la carpeta media
# Esto permite que se vean las fotos de los cafés en producción sin configurar un servidor externo.
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

# Tu manejador de errores 404
handler404 = 'api.views.mi_handler404'