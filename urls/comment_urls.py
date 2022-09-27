from django.urls import path

from apps.comment.views import (
    NewCommentView,
)


urlpatterns = [
    # login needed
    path('newcomment/<int:pk>/', NewCommentView.as_view(), name='new-comment'),
]
