from django.contrib import admin
from apps.post.models import Post


class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'date', '__str__')
	list_filter = ('user',)


admin.site.register(Post, PostAdmin)
