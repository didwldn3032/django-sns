from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *


@login_required
def follow_toggle(request, user_id):
    user = request.user
    followed_user = get_object_or_404(User, pk=user_id)
    is_follower = user.profile in followed_user.profile.followers.all()
    
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
        
    return redirect('home')



@login_required
def follow_list(request):
    followings = Profile.objects.filter(user=request.user)
    return render(request, 'users/list.html', {'followings':followings})

@login_required
def posts_list(request):
    posts_list = Post.objects.filter(user=request.user)
    return render(request, 'users/list3.html', {'posts_list':posts_list})

@login_required
def mypage(request):
    return render(request, 'users/mypage.html')


# Create your views here.
