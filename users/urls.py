from django.urls import path

from users.views import Profile, reqts

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('reqts/', reqts, name='reqts')

]
