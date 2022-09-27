from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from apps.post.forms import PostForm
from mixins import UserFromViewMixin


class NewPostView(LoginRequiredMixin, UserFromViewMixin, CreateView):
    form_class = PostForm
    template_name = 'post/new_post.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar'] = ['Enter text of a new post.', 'You can also attach multiple photos.']
        return context
