from django.urls import path
from .views import *

app_name="users"
urlpatterns = [
    path('<int:user_id>/follow_toggle/', follow_toggle, name="follow_toggle"),
    path('follow_list/', follow_list, name="follow_list"),
    path('posts_list/', posts_list, name="posts_list"),
    path('mypage/', mypage, name="mypage"),
]
