"""
Django settings for backend project.
Modificado para despliegue en AWS Elastic Beanstalk con RDS MySQL.
"""

import os
from pathlib import Path
# import dj_database_url  <- Ya no lo necesitamos, lo quitamos.

# BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# TEMPLATES
TEMPLATES_DIR = BASE_DIR / 'templates'  # Usando Path para consistencia

# ---------------------------------------------------------------------
# SEGURIDAD Y CONFIGURACIÓN DE HOSTS
# ---------------------------------------------------------------------

# Leemos la variable DEBUG (para EB, esto se puede configurar en la consola)
#DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
DEBUG = True  # Temporalmente en True para pruebas
# Permitimos '*' para que funcione con la URL de Elastic Beanstalk
ALLOWED_HOSTS = ["*"]

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
# BASE DE DATOS (Configuración para AWS RDS MySQL)
# ---------------------------------------------------------------------

# Hemos reemplazado la lógica de Azure/SQLite por la conexión directa a RDS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bd_isc5',                 # El nombre de tu BD
        'USER': 'adminisc',               # Tu usuario maestro de RDS
        'PASSWORD': '00sasuke00',         # Tu nueva contraseña
        'HOST': 'bd-isc5.cils0ssqwuu2.us-east-1.rds.amazonaws.com', # Tu Endpoint de RDS
        'PORT': '3306',
    }
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

STATIC_URL = '/static/'
# Esta ruta es la correcta para tu proyecto y para Elastic Beanstalk
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Usar WhiteNoise para manejar archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ---------------------------------------------------------------------
# USUARIO PERSONALIZADO Y LOGIN
# ---------------------------------------------------------------------
AUTH_USER_MODEL = 'usuarios.Usuario'
LOGIN_URL = 'login'

# ---------------------------------------------------------------------
# SEGURIDAD EXTRA (para despliegue)
# ---------------------------------------------------------------------
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Agregamos la URL de Elastic Beanstalk a los orígenes de confianza
# (aunque '*' en ALLOWED_HOSTS ya es bastante permisivo)
CSRF_TRUSTED_ORIGINS = [
    'https://*.azurewebsites.net',
    'http://*.elasticbeanstalk.com' # Agregamos esto para AWS
]