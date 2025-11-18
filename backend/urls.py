from django.contrib import admin
from django.urls import path, include, re_path
from api import views as api_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de tu app API
    path('api/', include('api.urls')),

    # --- PÁGINA PRINCIPAL REAL (DEBE SER PÚBLICA) ---
    path('', api_views.pagina_practica_view, name='inicio'),

    # --- AUTENTICACIÓN ---
    path('accounts/login/', api_views.login_view, name='login'),
    path('accounts/logout/', api_views.logout_view, name='logout'),
]

# archivos estáticos
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

handler404 = 'api.views.mi_handler404'
