from django.urls import path
from .views import *

app_name="users"
urlpatterns = [
    path('<int:user_id>/follow_toggle/', follow_toggle, name="follow_toggle"),
    path('following/<int:user_id>/', following, name="following"),
    path('follower/<int:user_id>/', follower, name="follower"),
    path('posts_list/<int:user_id>/', posts_list, name="posts_list"),
    path('<int:user_id>/profile/', profile, name="profile"),
]
