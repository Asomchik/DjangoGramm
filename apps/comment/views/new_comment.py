from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.comment.forms import CommentForm
from mixins import UserFromViewMixin


class NewCommentView(LoginRequiredMixin, UserFromViewMixin, CreateView):
    form_class = CommentForm
    template_name = 'post/post.html'

    def get_success_url(self):
        return f'{reverse_lazy("post", kwargs={"pk": self.object.post.pk})}#comments'
