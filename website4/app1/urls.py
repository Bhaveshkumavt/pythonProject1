from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.views.generic.base import RedirectView
from app1 import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    # path('home/', admin.site.urls),
    path('try_index/', views.HomeView.as_view()),
    path('index/', views.home, name='index'),
    path('notice/', views.NoticeListView.as_view()),
    path('notice/<int:pk>/', views.NoticeDetailView.as_view()),
    path('', RedirectView.as_view(url='index')),
    path('Profile/edit/<int:pk>', views.ProfileUpdateView.as_view(success_url='/app1/index')),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('sports/', views.sport, name='sports'),
    path('cricket/', views.cricket_view, name='cricket'),
    path('basketball/', views.basketball_view, name='basketball'),
    path('profile1/', views.profile_view, name='profile'),
    # path('login/', views.user_login, name='login'),
    path('login/', views.user_login, name='login'),


]
