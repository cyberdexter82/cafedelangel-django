# 👇 --- IMPORTACIONES MODIFICADAS --- 👇
from django.shortcuts import render, redirect
from django.contrib import messages
from usuarios.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Producto, Review # Asumo que Review está en api/models.py
from .forms import ReviewForm, ProfileForm # Asumo que tienes ProfileForm para el avatar
# --- ¡IMPORTACIONES NUEVAS PARA EL MANEJO DE ARCHIVOS! ---
from django.http import HttpResponseRedirect
from django.urls import reverse
# --- FIN DE IMPORTACIONES ---


# --- Vistas de tu aplicación ---

# 1. Vista para: login.html
def login_view(request):
    if request.user.is_authenticated:
        return redirect('buscador')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido de nuevo, {username}!')
                return redirect('buscador')
        # Si el form no es válido, el error se mostrará en el template
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})


# 2. Vista para: Buscador.html
@login_required
def buscador_view(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'Buscador.html', context)

# 3. Vista para: PaginaWeb PracticaMarcelo...html
@login_required
def pagina_practica_view(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'PaginaWeb PracticaMarcelo3-03-2025.html', context)

# 4. Vista para: OtraPaginaWeb1.html
@login_required
def otra_pagina_view(request):
    return render(request, 'OtraPaginaWeb1.html')

# 5. Vista para: Compra.html
@login_required
def compra_view(request):
    return render(request, 'Compra.html')

# 6. Vista para: reseñas.html (¡MODIFICADA PARA AÑADIR FORMULARIOS Y DATOS!)
@login_required
def resenas_view(request):
    # Obtener todas las reseñas ordenadas por fecha (más nuevas primero)
    reviews = Review.objects.all().select_related('user').order_by('-created_at')
    
    # Formulario para que el usuario suba una reseña nueva
    review_form = ReviewForm()
    
    # Formulario para subir/actualizar el avatar (asumo que existe ProfileForm en forms.py)
    # avatar_form = ProfileForm(instance=request.user.profile) 
    
    context = {
        'reviews': reviews,
        'review_form': review_form,
        # 'avatar_form': avatar_form, # Descomenta si usas ProfileForm
    }
    return render(request, 'resenas.html', context)


# -------------------------------------------------------------
# 🌟 NUEVA VISTA: Procesa el envío de la reseña
# -------------------------------------------------------------
@login_required
def dejar_resena(request):
    if request.method == 'POST':
        # Nota: Usamos request.FILES porque el formulario puede contener una imagen (MEDIA)
        form = ReviewForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user # Asigna el usuario logueado
            new_review.save()
            messages.success(request, '¡Gracias! Tu reseña se ha publicado con éxito.')
        else:
            messages.error(request, 'Error al procesar la reseña. Por favor, revisa los campos.')
    
    # Siempre redirige a la página de reseñas después de intentar el POST
    return redirect('resenas')


# -------------------------------------------------------------
# 🌟 NUEVA VISTA: Procesa la subida del avatar/perfil
# -------------------------------------------------------------
@login_required
def subir_avatar(request):
    if request.method == 'POST':
        # Asume que el usuario tiene un profile (se crea al registrarse o loguearse)
        try:
            profile_instance = request.user.profile
        except:
            messages.error(request, 'El perfil de usuario no existe. Intenta cerrar e iniciar sesión.')
            return redirect('resenas')

        # Usamos la instancia del perfil existente
        form = ProfileForm(request.POST, request.FILES, instance=profile_instance)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu avatar ha sido actualizado con éxito.')
        else:
            messages.error(request, 'Error al subir la imagen. Asegúrate de que el formato sea válido.')
    
    # Redirige a la página de donde vino el usuario
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('resenas')))


# 7. Vista para: Acerca.html
@login_required
def acerca_view(request):
    return render(request, 'Acerca.html')

# 8. Vista para: autores.html
@login_required
def autores_view(request):
    return render(request, 'autores.html')

# 9. Vista para 'cafe.html'
@login_required
def detalle_producto_view(request):
    return render(request, 'OtraPaginaWeb1.html') 

# 10. Vista para el error 404
def mi_handler404(request, exception):
    return render(request, '404.html', status=404)

# 11. VISTA DE REGISTRO
def registro_view(request):
    if request.user.is_authenticated:
        return redirect('inicio') 

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # 🌟 CREAR PERFIL: Aseguramos que tenga un perfil al registrarse
            # from .models import Profile # Necesitas importar Profile
            # Profile.objects.create(user=user) 
            
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'registro.html', {'form': form})

# 12. VISTA DE LOGOUT
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect('login')