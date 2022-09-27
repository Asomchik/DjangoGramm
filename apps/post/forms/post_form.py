from django import forms

from apps.post.models import Post, MediaContent
from mixins import UserToFormMixin


class PostForm(UserToFormMixin, forms.ModelForm):
    content = forms.ImageField(label='Attach photos', required=False, widget=forms.FileInput(
        attrs={
            'class': 'photos-field',
            'multiple': True,
        }))

    class Meta:
        model = Post
        fields = ['text']

    def save(self, commit=True, **kwargs):
        self.instance.user = self.user
        new_post = super().save(commit, **kwargs)
        files = getattr(self, 'files', None)
        if files:
            media_content = [
                MediaContent(post=new_post, content=file)
                for file in files.getlist('content', [])
            ]
            MediaContent.objects.bulk_create(media_content)
        return new_post
