from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import timedelta

def posts(request):
  post_list = Post.objects.all().order_by('-created_date')
  page = request.GET.get('page', 1)
  paginator = Paginator(post_list, 5)
  try:
    posts = paginator.page(page)
  except PageNotAnInteger:
    posts = paginator.page(1)
  except EmptyPage:
    posts = paginator.page(paginator.num_pages)
  return render(request, 'post_list.html', {'posts':posts})

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  time_check = (post.edited_date - post.created_date).seconds
  return render(request, 'post_detail.html', {'post':post, 'time_check':time_check})

@login_required
def post_add(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
      form = PostForm()
      return render(request, 'post_add.html', {'form':form})

@login_required
def post_edit(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if not request.user.username == post.author.username:
    return render(request, 'no_permission.html')
  else:
    if request.method == 'POST':
      form = PostForm(request.POST, instance=post)
      if form.is_valid():
        post = form.save(commit=False)
        post.save()
        if request.POST['next'] != '':
          next = request.POST['next']
        else:
          next = '/blog/posts/'
        return HttpResponseRedirect(next)
    else:
      form = PostForm(instance=post)
      return render(request, 'post_edit.html', {'form':form})

@login_required
def post_delete(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if not request.user.username == post.author.username:
    return render(request, 'no_permission.html')
  else:
    post.delete()
    return redirect('user_panel', request.user.username)

  