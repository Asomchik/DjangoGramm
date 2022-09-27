from django.contrib import messages as signals
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.user.forms import UserRegistrationForm


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            email = form.cleaned_data.get('email').lower()
            mail_subject = "Activate your DjangoGramm account."

            current_site = get_current_site(request)
            domain = current_site.domain
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            link = f'https://{domain}/activate/{uid}/{token}/'

            message = f'To finish creating your DjangoGramm account, ' \
                      f'confirm your email address by clicking this link: ' \
                      f'{link}'

            letter = EmailMessage(mail_subject, message, to=[email])
            letter.send(fail_silently=False)

            signals.success(request, f'Registration is almost complete.'
                                     f' Please, check your mail, and confirm registration.')
            context = {'sidebar': ['If you have not received an email within 5 minutes, check your ‘Spam’ folder.']}

            return render(request, 'base.html', context=context)
        else:
            signals.error(request, "Registration error")
    else:
        form = UserRegistrationForm()
    context = {'form': form,
               'sidebar': [f'After providing valid e-mail and strong password you will receive a message '
                           f'with a link to complete your registration.']}
    return render(request, 'user/registration.html', context=context)
