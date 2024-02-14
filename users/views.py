from django.shortcuts import render, redirect
from .forms import RegistrationForm


def register(request):
    """Регистрация пользователей"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin:login')
    else:
        # Если пользователь уже авторизован - редирект на главную страницу
        if not request.user.is_anonymous:
            return redirect('admin:index')
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
