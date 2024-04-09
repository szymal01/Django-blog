from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth import authenticate

def posts_list(request):
    if request.user.is_authenticated:
        posts = Post.objects.all().order_by('date')
    else:
        posts = Post.objects.filter(draft=False).order_by('date')
    return render(request, 'posts/posts_list.html', {'posts':posts})

def search(request):
    if request.method=="POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains=searched)
        return render(request, 'posts/search.html', {'searched':searched, 'posts':posts})
    else:
        return render(request, 'posts/search.html')

def post_detail(request, slug):
    #return HttpResponse(slug)
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {'post':post})

def post_update(request, slug):
        post = Post.objects.get(slug=slug)
        form = forms.UpdatePost(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('posts:list')
        return render(request, 'posts/post_update.html', {'post':post, 'form':form})

def post_delete(request, slug):
    post = Post.objects.get(slug=slug)
    post.delete()
    return render(request, 'posts/post_delete.html')

@login_required(login_url="/accounts/login/")
def comment_create(request):
    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts:list')
    else:
        form = forms.CreateComment()
    return render(request, 'posts/comment.html', {'form':form})

@login_required(login_url="/accounts/login/")
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_create.html', {'form':form})
