from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from apps.chat.forms import MessageForm
from apps.user.models import User
from mixins import UserFromViewMixin


class NewMessageView(LoginRequiredMixin, UserFromViewMixin, CreateView):
    form_class = MessageForm
    template_name = 'chat/new_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar'] = ['Create a new message to any of your friends.']
        if pk := self.kwargs.get('pk'):
            context['sidebar'] = ['Create a new message to your specific friend.']
            context['form'] = MessageForm(initial={'recipient': User.objects.get(pk=pk)})
        return context
