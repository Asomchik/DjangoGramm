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
