"""
Django settings for backend project.
"""

import os
from pathlib import Path

# BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔹 Templates
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# --- ¡CONFIGURACIÓN DE SEGURIDAD PARA AZURE! ---

# 1. Desactivar DEBUG para producción (CRÍTICO)
DEBUG = False 

# 2. Reemplaza 'nombre-de-tu-app' con el nombre que elegirás en Azure
ALLOWED_HOSTS = ['nombre-de-tu-app.azurewebsites.net'] 

# Clave Secreta - La reemplazaremos en Azure
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-&+7ia!=_s&c!h8&7j$xh74)c^o(u9=!d5rob2f&%ciux=(z-2)')


# APLICACIONES
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'usuarios',
]

# MIDDLEWARE (Añadimos WhiteNoise para estáticos)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <-- NUEVO: Para servir CSS/JS en Azure
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

# 🔹 TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# 🔹 CONFIGURACIÓN DE BASE DE DATOS (¡PostgreSQL en Azure!)
DATABASES = {
    'default': {
        # Usaremos PostgreSQL en producción
        'ENGINE': 'django.db.backends.postgresql', 
        
        # Azure nos dará estas variables de entorno con las credenciales:
        'NAME': os.environ.get('DB_NAME', 'db_local_dev'),
        'USER': os.environ.get('DB_USER', 'user_local_dev'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'pass_local_dev'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', 5432),
    }
}


# 🔹 Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🔹 Idioma y zona horaria
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 🔹 Clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔹 Modelo de usuario personalizado
AUTH_USER_MODEL = 'usuarios.Usuario'
LOGIN_URL = 'login'


# --- CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS Y MEDIA PARA PRODUCCIÓN ---

# 1. Dónde Django recogerá todos los archivos estáticos para Azure (la carpeta 'staticfiles')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Usamos el storage de WhiteNoise para comprimir y servir CSS/JS
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 2. Archivos de Media (Imágenes de productos subidas por el Admin)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')