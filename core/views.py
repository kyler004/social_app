from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Post, Like, Follow, Comment, Profile
from .forms import PostForm, CommentForm


# Create your views here.
#stopped at part 4.2

@login_required
def search(request):
    query = request.GET.get('q', '')
    users = User.objects.filter(username__icontains=query) if query else[]
    posts = Post.objects.filter(content__icontains=query) if query else []
    return render(request, 'core/search.html', {
        'query': query,
        'users': users,
        'posts': posts
    })

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get_or_create(user=user)[0]  # Get or create profile
    posts = Post.objects.filter(user=user).order_by('-created_at')
    followers = user.followers.count()
    following = user.following.count()
    is_following  = Follow.objects.filter(follower=request.user, followed=user).exists() if request.user.is_authenticated else False
    
    return render(request, "core/profile.html", {
        'user': user,
        'profile': profile,
        'posts': posts,
        'followers': followers,
        'following': following,
        'is_following': is_following
    })

@login_required
def home(request):
    # Show posts from followed users and the current user
    following = Follow.objects.filter(follower=request.user).values_list('followed', flat=True)
    posts = Post.objects.filter(user__in=following).order_by('-created_at') | Post.objects.filter(user=request.user).order_by('-created_at')
    post_form = PostForm()
    comment_form = CommentForm()
    return render(request, 'core/home.html', {'posts': posts, 'post_form': post_form, 'comment_form': comment_form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('core:home')
    return redirect('core:home')

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()  # Unlike if already liked
    return redirect('core:home')

@login_required 
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()
    return redirect('core:profile', username=request.user.username)

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('core:profile', username=request.user.username)
    else:
        form = PostForm(instance=post)
    return render(request, 'core/edit_post.html', {'form': form, 'post': post})

@login_required
def follow_user(request, user_id):
    followed_user = get_object_or_404(User, id=user_id)
    follow, created = Follow.objects.get_or_create(follower=request.user, followed=followed_user)
    if not created:
        follow.delete()  # Unfollow if already followed
    return redirect('core:home')

@login_required
def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
    return redirect('core:home')

@login_required
def share_post(request, post_id): 
    original_post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.user = request.user
            post.shared_post = original_post
            post.save()
    return redirect("core:home") 

@login_required
def logout_view(request):
    logout(request)
    return redirect("core:home")

def signup(request): 
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after signup
            return redirect("core:home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
