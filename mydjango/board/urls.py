from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #메인 페이지
    path('signup/', views.signup, name='signup'), #회원가입
    path('login/', views.user_login, name='login'), #로그인
    path('logout/', views.user_logout, name='logout'), #로그아웃

]