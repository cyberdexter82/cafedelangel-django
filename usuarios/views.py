from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('buscador')  # 👈 redirige a la vista principal en api
        else:
            messages.error(request, 'Credenciales incorrectas. Inténtalo de nuevo.')
    return render(request, 'login.html')
