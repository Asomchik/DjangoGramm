from django.db import models
from django.urls import reverse_lazy

from apps.user.models import User


class Message(models.Model):
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
	recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
	text = models.TextField(blank=False, null=False)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date']

	def get_absolute_url(self):
		return reverse_lazy('direct-user', kwargs={'pk': self.recipient.id})

	def __str__(self):
		return self.text
