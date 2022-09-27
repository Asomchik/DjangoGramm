from django.contrib import admin

from apps.user.models import User


class UserAdmin(admin.ModelAdmin):
	list_display = ('id', 'email', '__str__', 'bio', 'avatar')
	list_display_links = ('id', 'email', '__str__')
	search_fields = ('id', 'email', 'sender')
	# list_editable = (,)
	# list_filter = (,)


admin.site.register(User, UserAdmin)
