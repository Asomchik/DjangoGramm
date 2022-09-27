from django.contrib import admin

from apps.post.models import MediaContent


class MediaContentAdmin(admin.ModelAdmin):
	list_display = ('id', '__str__', 'post', 'content')
	list_filter = ('post',)


admin.site.register(MediaContent, MediaContentAdmin)
