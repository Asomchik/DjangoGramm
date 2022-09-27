from django import forms

from apps.comment.models import Comment
from mixins import UserToFormMixin


class CommentForm(UserToFormMixin, forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'post']
        widgets = {
            'post': forms.HiddenInput(),
            'text': forms.Textarea(
                attrs={
                    'class': 'comment-field',
                    'rows': 2,
                    'placeholder': 'Write your comment here'
                }),
        }

    def save(self, commit=True):
        self.instance.user = self.user
        new_comment = super().save(commit)
        return new_comment
