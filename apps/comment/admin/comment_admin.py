from django.contrib import admin

from apps.comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'date', 'post', '__str__')
	list_filter = ('user', 'post')


admin.site.register(Comment, CommentAdmin)
