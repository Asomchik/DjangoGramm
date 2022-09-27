from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.post.models import Post

from settings.settings import POSTS_PAGINATE_BY


class FeedView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post/posts.html'
    paginate_by = POSTS_PAGINATE_BY

    def _get_follows(self):
        return getattr(self.request.user, 'follows').all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar'] = ['Users you follow:'] + list(self._get_follows())
        return context

    def get_queryset(self):
        return Post.objects.filter(user__in=self._get_follows()).order_by('-date')
