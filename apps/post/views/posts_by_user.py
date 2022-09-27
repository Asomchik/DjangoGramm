from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from apps.post.models import Post
from apps.user.models import User


from settings.settings import POSTS_PAGINATE_BY


class UsersPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post/posts.html'
    paginate_by = POSTS_PAGINATE_BY

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar'] = [f'All posts of {get_object_or_404(User, id=self.kwargs["pk"])} sorted by date.']
        return context

    def get_queryset(self):
        return Post.objects.filter(user_id=self.kwargs['pk']).order_by('-date')
