from django.shortcuts import render, redirect
from .models import Post, Block, Comment, BlogUser, File, User
from .forms import PostForm, BlockForm


# Create your views here.
def posts(request):
    blocked = Block.objects.filter(blocker__user=request.user).values('blocked__user')
    query_set = Post.objects.exclude(user__user__in=blocked).exclude(user__user=request.user).order_by("-creation_date")
    context = {
        "posts": query_set,
        "comments": Comment.objects.all()
    }
    return render(request, "posts.html", context=context)


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user = BlogUser.objects.get(user=request.user)
            post.user = user
            post.save()
            return redirect("profile")
    else:
        form = PostForm()
    context = {"form": form}
    return render(request, "add_post.html", context=context)


def profile(request):
    user_profile = BlogUser.objects.get(user=request.user)
    query_set = Post.objects.filter(user__user=request.user).order_by("-creation_date")
    context = {"user_profile": user_profile, "posts": query_set}
    return render(request, "profile.html", context=context)


def blocked_users(request, user_id=None):
    if user_id is not None:
        block = Block.objects.get(blocker__user=request.user, blocked__user__id=user_id)
        block.delete()
        return redirect("blocked_users")
    if request.method == "POST":
        form = BlockForm(request.POST)
        if form.is_valid():
            block = form.save(commit=False)
            user = BlogUser.objects.get(user=request.user)
            block.blocker = user
            block.save()
            return redirect("blocked_users")
    else:
        form = BlockForm()
    blocked = Block.objects.filter(blocker__user=request.user).values('blocked__user')
    query_set = BlogUser.objects.filter(user__id__in=blocked)
    context = {"blocked_users": query_set, "form": form}
    return render(request, "blocked_users.html", context=context)
