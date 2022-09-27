from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .chat_urls import urlpatterns as chat_urls
from .comment_urls import urlpatterns as comment_urls
from .post_urls import urlpatterns as post_urls
from .user_urls import urlpatterns as user_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(user_urls)),
    path('', include(post_urls)),
    path('', include(comment_urls)),
    path('direct/', include(chat_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # import debug_toolbar
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),
