from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Post
from .forms import (
    CommentForm,
    PostForm,
    EditProfileForm,
    LoginForm,
    RegisterForm,
    SearchForm,
)
from django.http import HttpResponseRedirect

# Create your views here.


def loginPage_view(request):
    if request.user.is_authenticated:
        return redirect("main:home")

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist.")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main:home")
        else:
            messages.error(request, "Username or password is incorrect.")
    login_form = LoginForm()

    context = {"login_form": login_form}

    return render(request, "main/login.html", context=context)


@login_required(login_url="main:login")
def logout_view(request):
    logout(request)
    return redirect("main:login")


def registerPage_view(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            profile = Profile(user=user)
            profile.save()
            login(request, user)
            return redirect("main:home")
        else:
            messages.error(request, "An error occurred while registration.")

    context = {"form": form}
    return render(request, "main/register.html", context=context)


@login_required(login_url="main:login")
def home_view(request):
    if not request.user.is_authenticated:
        return redirect("main:login")
    search_form = SearchForm()
    user_profile = Profile.objects.get(user=request.user)
    
    posts = Post.objects.all()
    if request.method == "POST":
        like_post_pk = request.POST.get("like")
        dislike_post_pk = request.POST.get("dislike")
        search_form = SearchForm(request.POST)
        if like_post_pk:
            post = Post.objects.get(pk=like_post_pk)
            user_profile.like(post)
        elif dislike_post_pk:
            post = Post.objects.get(pk=dislike_post_pk)
            user_profile.dislike(post)
        elif search_form.is_valid():
            search = dict(search_form.data.items())["search"]
            posts = Post.objects.filter(title__contains=search)
            search_form = SearchForm()

    liked_post_list = [i.post for i in request.user.likes.all()]
    disliked_post_list = [i.post for i in request.user.dislikes.all()]
    
    
    context = {
        "posts": posts,
        "search_form": search_form,
        "liked_post_list": liked_post_list,
        "disliked_post_list": disliked_post_list,
    }
    return render(request, "main/home.html", context=context)


def about_view(request):
    return render(request, "main/about.html")


@login_required(login_url="main:login")
def show_post_view(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comments.all()  # type: ignore

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = Profile.objects.get(user=request.user)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(f"/post/{pk}/")
    else:
        comment_form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "comment_form": comment_form,
    }

    return render(request, "main/post.html", context=context)


@login_required(login_url="main:login")
def edit_post_view(request, pk):
    post = Post.objects.get(pk=pk)
    edit_post_form = PostForm(instance=post)

    if request.method == "POST":
        edit_post_form = PostForm(request.POST)
        if edit_post_form.is_valid():
            new_post = edit_post_form.save(commit=False)

            post.title = new_post.title
            post.subtitle = new_post.subtitle
            post.body = new_post.body
            post.header_image_url = new_post.header_image_url
            post.save()
            return redirect("main:home")

    context = {"edit_post_form": edit_post_form}
    return render(request, "main/edit_post.html", context=context)


@login_required(login_url="main:login")
def create_post_view(request):
    if request.method == "POST":
        create_post_form = PostForm(request.POST)
        if create_post_form.is_valid():
            new_post = create_post_form.save(commit=False)
            profile = Profile.objects.get(user=request.user)
            new_post.author = profile
            new_post.save()

            return redirect("main:home")
    else:
        create_post_form = PostForm()

    context = {"create_post_form": create_post_form}
    return render(request, "main/create_post.html", context=context)


@login_required(login_url="main:login")
def delete_post_view(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()

    return redirect("main:home")


@login_required(login_url="main:login")
def profile_view(request, pk):
    profile = Profile.objects.get(user=User.objects.get(pk=pk))
    context = {"profile": profile}
    return render(request, "main/profile.html", context=context)


@login_required(login_url="main:login")
def edit_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    edit_profile_form = EditProfileForm(instance=profile)
    if request.method == "POST":
        edit_profile_form = EditProfileForm(request.POST)
        if edit_profile_form.is_valid():
            new_profile = edit_profile_form.save(commit=False)
            profile.about = new_profile.about
            profile.save()
            return redirect("main:profile", profile.pk)

    context = {
        "profile": profile,
        "edit_profile_form": edit_profile_form,
    }

    return render(
        request,
        "main/edit_profile.html",
        context=context,
    )
