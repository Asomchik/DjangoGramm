from django.urls import path

from apps.chat.views import MessagesView, NewMessageView, UsersMessagesView


urlpatterns = [
    # login needed
    path('', MessagesView.as_view(), name='direct'),
    path('<int:pk>/', UsersMessagesView.as_view(), name='direct-user'),
    path('createmssg/', NewMessageView.as_view(), name='create-message'),
    path('createmssg/<int:pk>/', NewMessageView.as_view(), name='create-message'),
]
