from django.shortcuts import render, redirect
from setuptools.command.register import register

from .froms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import User

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data.get('email'),
                                password=form.cleaned_data.get('password1'))
            login(request, user)

            messages.success(request, f"Поздравляю {user.username}, Ваш аккаунт успешно создан")

            return redirect('core:index')

    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/sign-up.html', {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Вы успешно авторизались")
                return redirect("core:index")
            else:
                messages.warning(request, f"Пользователь не найден")
        except:
            messages.warning(request, f"Пользователь с таким {email} не существует")



    return render(request, "authentication/sign-in.html", )


def logout_view(request):
    logout(request)
    messages.success(request, "Вы вышли из системы")
    return redirect("authentication:sign.in")

