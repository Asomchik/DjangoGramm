from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy

from .usermanager import UserManager


def user_directory_path(instance, filename):
    user_id = instance.id
    return f'user_{user_id}/{filename}'


class User(AbstractUser):
    objects = UserManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
    username = None
    email = models.EmailField(blank=False, null=False, unique=True)

    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=256, blank=False, null=False)
    bio = models.TextField("Biography", blank=True, null=True)
    avatar = models.ImageField(
        upload_to=user_directory_path,
        default='default/avatar.jpg', blank=True, null=True
    )

    # followers system
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('user-posts', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
