from django.db import models
from django.urls import reverse_lazy

from apps.user.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(unique_for_date='date', blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse_lazy('post', kwargs={'pk': self.id})

    def __str__(self):
        return self.text[:25] + "..."
