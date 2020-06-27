from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from blog.models import Post

class PostInline(admin.StackedInline):
  model = Post
  extra = 0

class CustomUserAdmin(UserAdmin):
  inlines = [PostInline]
  list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)