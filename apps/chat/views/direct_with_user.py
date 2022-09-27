from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from apps.chat.models import Message
from apps.user.models import User
from settings.settings import MESSAGES_PAGINATE_BY


class UsersMessagesView(LoginRequiredMixin, ListView):
    template_name = 'chat/direct.html'
    paginate_by = MESSAGES_PAGINATE_BY

    def get_queryset(self):
        return Message.objects.filter(
            Q(recipient_id=self.request.user.id, sender_id=self.kwargs['pk']) |
            Q(recipient_id=self.kwargs['pk'], sender_id=self.request.user.id)
            ).order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar'] = ['Conversation with specific user.']
        if companion := get_object_or_404(User, id=self.kwargs['pk']):
            context['chat_title'] = f'Chat with {companion}'
            context['sender_id'] = companion.id
        return context
