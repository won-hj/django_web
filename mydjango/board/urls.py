from django.urls import path
from . import views
from .views import post_list, post_detail, post_create, post_edit, post_delete

urlpatterns = [
    #path('', views.index, name='index'), #메인 페이지
    path('', post_list, name='post_list'),# 루트 페이지를 게시글 목록으로 설정
    path('signup/', views.signup, name='signup'), #회원가입
    path('login/', views.user_login, name='login'), #로그인
    path('logout/', views.user_logout, name='logout'), #로그아웃
    path('<int:post_id>/', post_detail, name='post_detail'), #게시글 상세
    path('new/', post_create, name='post_create'), #글쓰기페이지 추가
    path('<int:post_id>/edit/', post_edit, name='post_edit'), #수정기능추가
    path('<int:post_id>/delete/', post_delete, name='post_delete'), #삭제기능추가
]