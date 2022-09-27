from django.contrib import messages as signals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from apps.user.forms import UserProfileForm
from apps.user.models import User


@login_required()
def profile(request):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            signals.success(request, "Your profile information has been updated.")
        else:
            signals.error(request, 'Error in some fields')
    else:
        form = UserProfileForm(instance=user)

    context = {'form': form,
               'user': request.user,
               'sidebar': ['You can edit your profile info here.', 'E-mail is not editable.'],
               }
    return render(request, 'user/profile.html', context=context)
