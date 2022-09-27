from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import ListView

from apps.post.models import Post
from settings.settings import POSTS_PAGINATE_BY


class PopularPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post/posts.html'
    paginate_by = POSTS_PAGINATE_BY

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar'] = ['All posts sorted by number of likes.']
        return context

    def get_queryset(self):
        return Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes', '-date')
