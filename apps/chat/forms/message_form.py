from django import forms

from apps.chat.models import Message
from apps.user.models import User
from mixins import UserToFormMixin


class MessageForm(UserToFormMixin, forms.ModelForm):
    recipient = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        if recipient := kwargs.get('initial').get('recipient'):
            self.fields['recipient'].queryset = User.objects.filter(pk=recipient.id)
        else:
            self.fields['recipient'].queryset = self.user.follows.all()

    class Meta:
        model = Message
        fields = ['text', 'recipient']

    def save(self, commit=True):
        self.instance.sender = self.user
        return super().save(commit)
