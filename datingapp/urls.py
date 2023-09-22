# urls.py

from django.urls import path
from . import views
from .views import register_view, login_view
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.index, name='index'),
    path('like/<int:user_id>/', views.like_user, name='like_user'),
    path('mutual_likes/', views.mutual_likes, name='mutual_likes'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='datingapp:login'), name='logout'),

]
