from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post


# Create your views here.
def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts':posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_blogs')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form':form})

def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    name = post.name
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = name
            post.save()
            return redirect('view_blogs')
    else:
        form = PostForm(instance=post)
    return render(request, 'add_post.html', {'form':form})


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('view_blogs')