from django.contrib import messages as signals
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.shortcuts import redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from apps.user.models import User


def activate(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    result = PasswordResetTokenGenerator().check_token(user=user, token=token)
    if result:
        user.is_active = True
        user.save()
        signals.success(request, f'Your registration complete. You may login now.')
    else:
        signals.error(request, f'Your registration link is invalid')
    return redirect('login')
