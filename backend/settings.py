"""
Django settings for backend project.
Configurado para despliegue en Azure App Service.
"""

import os
from pathlib import Path
import dj_database_url

# BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# TEMPLATES
TEMPLATES_DIR = BASE_DIR / 'templates'  # Usando Path para consistencia

# ---------------------------------------------------------------------
# SEGURIDAD Y CONFIGURACIÓN DE HOSTS
# ---------------------------------------------------------------------

# Leemos la variable DEBUG desde Azure
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = ["*"]  # En producción, especifica hosts explícitos

# SECRET_KEY
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-7ia!=_s&c!h8&7j$xh74)c^o(u9=!d5rob2f&%ciux=(z-2)"
)

# ---------------------------------------------------------------------
# APLICACIONES
# ---------------------------------------------------------------------
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

# ---------------------------------------------------------------------
# MIDDLEWARE
# ---------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Sirve CSS/JS estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

# ---------------------------------------------------------------------
# TEMPLATES
# ---------------------------------------------------------------------
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

# ---------------------------------------------------------------------
# BASE DE DATOS (Conexión a PostgreSQL en Azure o SQLite local)
# ---------------------------------------------------------------------
if os.environ.get('DB_HOST'):
    # Configuración para PostgreSQL usando variables de entorno de Azure
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT', '5432'),
            'OPTIONS': {'sslmode': 'require'},  # SSL para Azure
        }
    }
else:
    # Configuración para SQLite local
    DATABASES = {
        'default': dj_database_url.config(
            default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
            conn_max_age=600
        )
    }

# ---------------------------------------------------------------------
# VALIDACIÓN DE CONTRASEÑAS
# ---------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------------------------------------------------------------
# CONFIGURACIONES REGIONALES
# ---------------------------------------------------------------------
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------------------------------------------------------------
# ARCHIVOS ESTÁTICOS Y MEDIA
# ---------------------------------------------------------------------
# ¡Cambio del "Truco del Prefijo"!
STATIC_URL = '/'  # Servimos los estáticos desde la raíz para evitar problemas en Azure
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Usando Path

# Usar WhiteNoise para manejar archivos estáticos con mejor cacheo
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ---------------------------------------------------------------------
# USUARIO PERSONALIZADO Y LOGIN
# ---------------------------------------------------------------------
AUTH_USER_MODEL = 'usuarios.Usuario'
LOGIN_URL = 'login'

# ---------------------------------------------------------------------
# SEGURIDAD EXTRA (recomendado para producción)
# ---------------------------------------------------------------------
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Usamos un comodín para aceptar la URL larga de Azure
CSRF_TRUSTED_ORIGINS = ['https://*.azurewebsites.net']
