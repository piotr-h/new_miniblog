from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
  path('posts/', views.posts, name='posts'),
  path('posts/<int:pk>/', views.post_detail, name='post_detail'),
  path('', RedirectView.as_view(url='posts/', permanent=True)),
  path('posts/<int:pk>/delete', views.post_delete, name='post_delete'),
  path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
  path('posts/add/', views.post_add, name='post_add',)
] 

