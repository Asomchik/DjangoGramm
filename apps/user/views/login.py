from django.contrib import messages as signals
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from apps.user.forms import LoginForm
from apps.user.models import User


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password')
            user = None
            if User.objects.filter(email=email).exists():
                if not User.objects.get(email=email).is_active:
                    signals.error(request, 'You should activate your account first. Follow the email instruction.')
                else:
                    user = authenticate(email=email, password=raw_password)
            if user is not None:
                auth_login(request, user)
                return redirect(request.GET.get('next', 'feed'))
            else:
                signals.error(request, 'Error in name or password')
        else:
            signals.error(request, 'Error(s) in form')
    else:
        form = LoginForm()

    context = {'form': form,
               'sidebar': ['Use e-mail 1@sample.com', 'and password 1', 'to log in.'],
               }
    return render(request, 'user/login.html', context=context)
