from django.urls import path

from apps.user.views import login, registration, logout, profile, activate


urlpatterns = [
    # no login needed
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
    path('activate/<str:uid64>/<str:token>/', activate, name='activate'),

    # login needed
    path('profile/', profile, name='profile'),
]
