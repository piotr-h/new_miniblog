from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, BioForm
from .models import CustomUser
from blog.models import Post
from django.contrib.auth.decorators import login_required

def signup(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = CustomUserCreationForm
    return render(request, 'signup.html', {'form':form})

def author_detail(request, username):
  details = CustomUser.objects.get(username=username)
  post_list = Post.objects.filter(author__username=username)
  context = {
    'details':details,
    'post_list':post_list
  }
  return render(request, 'author_detail.html', context)

def author_list(request):
  details = CustomUser.objects.all().order_by('id')
  return render(request, 'author_list.html', {'details':details})

@login_required
def user_panel(request, username):
  if not request.user.username == username:
    return render(request, 'no_permission.html')
  else:
    details = CustomUser.objects.get(username=username)
    post_list = Post.objects.filter(author__username=username)
    context = {
      'details':details,
      'post_list':post_list
    }
    return render(request, 'user_panel.html', context)

@login_required
def bio_edit(request, username):
  if not request.user.username == username:
    return render(request, 'no_permission.html')
  else:
    details = CustomUser.objects.get(username=username)
    if request.method == 'POST':
      form = BioForm(request.POST, request.FILES, instance=details)
      if form.is_valid():
        details = form.save()
        details.save()
        return redirect('user_panel', request.user.username)
    else:
      form = BioForm(instance=details)
      return render(request, 'bio_edit.html', {'form':form})
