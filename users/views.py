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
    followings = Profile.objects.all().first()
    following_list = user.followings.all()
    return render(request, 'users/list.html', {'followings':followings})

@login_required
def posts_list(request):
    posts_list = Post.objects.filter(user=request.user)
    return render(request, 'users/list3.html', {'posts_list':posts_list})


@login_required
def profile(request, user_id):
    user = request.user
    post_user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/profile.html')

# 그 제 아이디 기준으로 마이페이지 하는거는 가능한데 글 쓴 사람의 아이디를 받아서 마이페이지를 가는게
# 어렵더라고요 id를 어떻게 받아와야할지 모르겠어서 두개로 나눠서 내꺼 가는거랑 글 쓴 사람 가는거로 하려 했어요
# 그요면 나중에 페이지 하나 더 만드려는거야?
# 저거 그대로 사용하는데 그 글쓴 사람꺼는 url에 아이디까지 붙는 형식으로...?
# 사실 원래 의도는 mypage/user_id형태였는데 id받는것 땜에 일단 내 마이페이지라도 만들자는 심정으로 했습니다...
# 아 맞아요 원래 마이페이지 안에 저거 세개 다 들어가는건데 뭐 하다가 세개로 또 나눠서... 맞네요 마이페이지는 둘다 동일해도 괜찮네요
# 글 목록, 팔로우 관련 목록이 user_id형식으로 가야겠네요


# 음... 어떻게 진행하려는지 아직 감이 안 잡히기는 한데
# 내가 볼 떄는, 우리가 해야할게 사용자 이름을 눌렀을 때 그 사용자의 프로필이 들어있는 페이지로 이동하는거잖아
# 그 페이지를 user_profile.html이라고 우선 해볼게
# 근데 그 페이지는 나의 프로필 페이지랑도 화면 구성이 똑같아
# 다만 내가 팔로우한 사람, 나를 팔로우한 사람 등의 추가 기능이 있을 뿐이지
# 그러면 mypage를 mypage, mypage2로 나눌 필요없이 그냥 post.user.id 를 넘기느냐
# 아니면 그냥 현재 유저인 request.user.id를 넘기느냐 차이니까 user_id 하나만 넘겨주면 되는거야