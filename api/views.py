# api/views.py

# 👇 --- IMPORTACIONES MODIFICADAS --- 👇
from django.shortcuts import render, redirect
from django.contrib import messages
from usuarios.forms import CustomUserCreationForm
# --- ¡IMPORTACIONES NUEVAS PARA EL LOGIN Y LOGOUT! ---
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# --- 👇 ¡IMPORTACIÓN NUEVA PARA PROTEGER VISTAS! 👇 ---
from django.contrib.auth.decorators import login_required
# --- 👇 ¡IMPORTACIÓN NUEVA PARA TUS PRODUCTOS! 👇 ---
from .models import Producto
# --- FIN DE IMPORTACIONES ---


# --- Vistas de tu aplicación ---

# 1. Vista para: login.html (PÚBLICA - NO SE TOCA)
def login_view(request):
    # Si el usuario ya está logueado, lo mandamos al buscador
    if request.user.is_authenticated:
        return redirect('buscador')

    if request.method == 'POST':
        # Si se envía el formulario (POST)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Si el formulario es válido...
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # ...autenticamos al usuario
            user = authenticate(username=username, password=password)
            
            if user is not None:
                # ...si el usuario existe, iniciamos sesión
                login(request, user)
                messages.success(request, f'¡Bienvenido de nuevo, {username}!')
                # Y lo mandamos al buscador
                return redirect('buscador')
        else:
            # Si el form no es válido (contraseña mal, usuario no existe)
            # el 'form.non_field_errors' en el HTML mostrará el error.
            pass
    else:
        # Si es la primera carga (GET), mostramos un formulario vacío
        form = AuthenticationForm()
        
    # Renderizamos 'login.html' y le pasamos el 'form'
    return render(request, 'login.html', {'form': form})


# 2. Vista para: Buscador.html (¡MODIFICADA!)
@login_required
def buscador_view(request):
    # Consultamos todos los productos de la base de datos
    productos = Producto.objects.all()
    # Los pasamos al template
    context = {'productos': productos}
    return render(request, 'Buscador.html', context)

# 3. Vista para: PaginaWeb PracticaMarcelo...html (¡MODIFICADA!)
@login_required
def pagina_practica_view(request):
    # Consultamos todos los productos de la base de datos
    productos = Producto.objects.all()
    # Los pasamos al template en un 'context'
    context = {'productos': productos}
    return render(request, 'PaginaWeb PracticaMarcelo3-03-2025.html', context)

# 4. Vista para: OtraPaginaWeb1.html (¡PROTEGIDA!)
@login_required
def otra_pagina_view(request):
    return render(request, 'OtraPaginaWeb1.html')

# 5. Vista para: Compra.html (¡PROTEGIDA!)
@login_required
def compra_view(request):
    return render(request, 'Compra.html')

# 6. Vista para: reseñas.html (¡PROTEGIDA!)
@login_required
def resenas_view(request):
    return render(request, 'reseñas.html')

# 7. Vista para: Acerca.html (¡PROTEGIDA!)
@login_required
def acerca_view(request):
    return render(request, 'Acerca.html')

# 8. Vista para: autores.html (¡PROTEGIDA!)
@login_required
def autores_view(request):
    return render(request, 'autores.html')

# 9. Vista para 'cafe.html' (¡PROTEGIDA!)
@login_required
def detalle_producto_view(request):
    return render(request, 'OtraPaginaWeb1.html') 

# 10. Vista para el error 404 (PÚBLICA - NO SE TOCA)
def mi_handler404(request, exception):
    return render(request, '404.html', status=404)

# --- 11. VISTA DE REGISTRO (PÚBLICA - NO SE TOCA) ---
def registro_view(request):
    # Si el usuario ya está logueado, lo mandamos al inicio
    if request.user.is_authenticated:
        return redirect('inicio') 

    if request.method == 'POST':
        # Si el formulario se envía (POST), crea una instancia con los datos
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido...
            form.save() # ...guarda el nuevo usuario en la base de datos
            
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            
            # Redirige al usuario a la página de login
            return redirect('login')
    else:
        # Si es la primera vez que carga la página (GET), crea un formulario vacío
        form = CustomUserCreationForm()
        
    # Renderiza el 'registro.html' y le pasa el formulario
    return render(request, 'registro.html', {'form': form})

# --- 12. VISTA DE LOGOUT (PÚBLICA - NO SE TOCA) ---
def logout_view(request):
    logout(request) # Django borra la sesión del usuario
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect('login') # Lo mandamos de vuelta al login