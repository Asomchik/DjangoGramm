from django.contrib import admin

from apps.chat.models import Message


class MessageAdmin(admin.ModelAdmin):
	list_display = ('id', 'date', 'sender', 'recipient', 'text')
	list_filter = ('sender', 'recipient')


admin.site.register(Message, MessageAdmin)
