# views.py
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import CustomUser, Like
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()
@login_required(login_url='/login')
def index(request):
    users = User.objects.exclude(id=request.user.id)

    liked_users_ids = Like.objects.filter(from_user=request.user).values_list('to_user_id', flat=True)
    if request.user.gender == 'М':
        users = users.exclude(id__in=liked_users_ids).filter(gender='Ж')
    else:
        users = users.exclude(id__in=liked_users_ids).filter(gender='М')
    return render(request, 'users/index.html', {'users': users})

@login_required(login_url='/login')
def like_user(request, user_id):
    to_user = get_object_or_404(User, id=user_id)
    Like.objects.create(from_user=request.user, to_user=to_user)
    return HttpResponseRedirect(reverse('datingapp:index'))
    return redirect('/')

@login_required(login_url='/login')
def mutual_likes(request):
    likes_sent = request.user.likes_sent.all()
    mutual_likes = [like for like in likes_sent if Like.objects.filter(from_user=like.to_user, to_user=request.user).exists()]
    return render(request, 'users/mutual_likes.html', {'mutual_likes': mutual_likes})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})