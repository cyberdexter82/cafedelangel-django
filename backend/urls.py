from django.contrib import admin
from django.urls import path, include
from api import views as api_views

# --- 1. IMPORTACIONES NUEVAS ---
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),

    path('', api_views.login_view, name='inicio'),
]

# --- 2. LÍNEA NUEVA AÑADIDA AL FINAL ---
# Esta línea le dice a Django que sirva los archivos de tu carpeta 'static'
# MIENTRAS estés en modo DEBUG.
if settings.DEBUG:
    # Esto es para tu CSS y JS (archivos estáticos)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    
    # --- 👇 ¡ESTA ES LA LÍNEA NUEVA AÑADIDA! 👇 ---
    # Esto es para las imágenes de productos (archivos media)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# --- 3. (Esto ya lo tenías, asegúrate que se quede) ---
handler404 = 'api.views.mi_handler404'
