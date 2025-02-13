from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post #Post 모델 가져오기
from .forms import PostForm #폼추가


# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'board/index.html') #HttpResponse('게시판 페이지')

#회원가입
def signup(request):
    if request.method == "POST":
        username= request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, '존재하는 사용자입니다.')
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password1)
        user.save()
        messages.success(request, '회원가입이 완료되었습니다.')
        return redirect('login')

    return render(request, 'board/signup.html')

#로그인
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if not user:
            messages.error(request, '로그인 정보가 올바르지 않습니다.')
            return redirect('login')
        else:
            login(request, user)
            messages.success(request, '로그인되었습니다.')
            return redirect('index')

    return render(request, 'board/login.html')

#로그아웃
def user_logout(request):
    logout(request)
    messages.success(request, '로그아웃 되었습니다.')
    return redirect('index')


def post_list(request):
    posts = Post.objects.all().order_by("-created_at") #최신 글부터 정렬
    return render(request, "board/post_list.html", {"posts":posts}) #템플릿에 전달

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "board/post_detail.html", {"post": post}) #템플릿에 전달; set가 아니라 dict여야만 한다


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list') #저장 후 게시글 목록으로 이동
    else:
        form = PostForm()

    return render(request, 'board/post_form.html', {'form': form})

def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id) #수정 후 해당 게시글 이동

    else:
        form = PostForm(instance=post)

    return render(request, 'board/post_form.html', {'form':form})