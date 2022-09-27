from django.urls import path
from django.views.generic import RedirectView

from apps.post.views import (
    PopularPostsView,
    UsersPostsView,
    PostView,
    NewPostView,
    FeedView,
)


urlpatterns = [
    # redirect index page
    path('', RedirectView.as_view(pattern_name='feed')),

    # login needed
    path('feed/', FeedView.as_view(), name='feed'),
    path('popular/', PopularPostsView.as_view(), name='popular-posts'),

    path('user/<int:pk>/', UsersPostsView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostView.as_view(), name='post'),
    path('newpost/', NewPostView.as_view(), name='new-post'),
]
