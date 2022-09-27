from django.db import models

from .post import Post


def user_directory_path(instance, filename):
    user_id = instance.post.user.id
    return f'user_{user_id}/{filename}'


class MediaContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return f'Photo for post {self.post.id}'
