from django.shortcuts import render, redirect
from django.contrib import messages
from usuarios.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Producto, Review, Profile 
from .forms import ReviewForm, ProfileForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist


# 1. Vista para: login.html
def login_view(request):
    if request.user.is_authenticated:
        return redirect('pagina_practica')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido de nuevo, {username}!')
                return redirect('pagina_practica')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})


# 2. Vista para: Buscador.html
@login_required
def buscador_view(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'Buscador.html', context)


# 3. Vista para: Pagina principal - SIN LOGIN REQUIRED (corrección)
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


# 6. Vista para: reseñas.html
@login_required
def resenas_view(request):
    reviews = Review.objects.all().select_related('user').order_by('-created_at')
    review_form = ReviewForm()
    
    context = {
        'reviews': reviews,
        'review_form': review_form,
    }
    return render(request, 'resenas.html', context)


# Procesa el envío de la reseña
@login_required
def dejar_resena(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.save()
            messages.success(request, '¡Gracias! Tu reseña se ha publicado con éxito.')
        else:
            messages.error(request, 'Error al procesar la reseña. Por favor, revisa los campos.')
    
    return redirect('resenas')


# Procesa la subida de avatar
@login_required
def subir_avatar(request):
    if request.method == 'POST':
        try:
            profile_instance = request.user.profile
        except Profile.DoesNotExist:
            messages.error(request, 'El perfil de usuario no existe. Intenta cerrar e iniciar sesión.')
            return redirect('resenas')

        form = ProfileForm(request.POST, request.FILES, instance=profile_instance)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu avatar ha sido actualizado con éxito.')
        else:
            messages.error(request, 'Error al subir la imagen. Asegúrate de que el formato sea válido.')
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('resenas')))


# 7. Vista para: Acerca.html
@login_required
def acerca_view(request):
    return render(request, 'Acerca.html')


# 8. Vista para: autores.html
@login_required
def autores_view(request):
    return render(request, 'autores.html')


# 9. Vista para: cafe.html
@login_required
def detalle_producto_view(request):
    return render(request, 'OtraPaginaWeb1.html') 


# 10. Vista para error 404
def mi_handler404(request, exception):
    return render(request, '404.html', status=404)


# 11. Vista de registro
def registro_view(request):
    if request.user.is_authenticated:
        return redirect('pagina_practica')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')
        else:
            messages.error(request, 'Error al registrar el usuario. Por favor, revisa los campos.')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'registro.html', {'form': form})


# 12. Vista de LOGOUT (FUNCIONANDO)
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect('inicio')   # ← ahora te manda a la página principal


# Vista de perfil
@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Perfil actualizado con éxito!')
            return redirect('perfil')
        else:
            messages.error(request, 'Error al actualizar el perfil.')
    else:
        form = ProfileForm(instance=profile)
        
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'perfil.html', context)
