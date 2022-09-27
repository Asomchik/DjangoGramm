class UserToFormMixin:
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        return super().__init__(*args, **kwargs)
