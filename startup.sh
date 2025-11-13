#!/bin/bash

# Script de inicio para Azure App Service
# Este script SOLO prepara la aplicación (migraciones y archivos estáticos)
# NO inicia el servidor - eso lo hace Azure con el comando de inicio

echo "=========================================="
echo "Iniciando preparación de la aplicación..."
echo "=========================================="

# Activar el entorno virtual si existe
if [ -d "/home/site/wwwroot/antenv" ]; then
    echo "Activando entorno virtual..."
    source /home/site/wwwroot/antenv/bin/activate
fi

# Navegar al directorio del proyecto
cd /home/site/wwwroot

echo "Aplicando migraciones de base de datos..."
python manage.py migrate --noinput

echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "=========================================="
echo "Preparación completada exitosamente"
echo "=========================================="

# NO ejecutar gunicorn aquí - Azure lo hará automáticamente
#no se 
