from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.comment.forms import CommentForm
from apps.post.models import Post


class PostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post/post.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar'] = ['Images are clickable (opening full-size in a new tab).',
                              'You can add a comment to a post using form under the post.']
        context['form'] = CommentForm(initial={'post': Post.objects.get(pk=self.kwargs['pk'])})
        return context
