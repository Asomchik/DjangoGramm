from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView

from apps.chat.models import Message
from settings.settings import MESSAGES_PAGINATE_BY


class MessagesView(LoginRequiredMixin, ListView):
    template_name = 'chat/direct.html'
    paginate_by = MESSAGES_PAGINATE_BY

    def get_queryset(self):
        return Message.objects.filter(
            Q(recipient_id=self.request.user.id) |
            Q(sender_id=self.request.user.id)
            ).order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar'] = ['All the messages sorted by time.',
                              'You can see your chat with a person by clicking on their name.']
        context['chat_title'] = "All your messages"
        return context
