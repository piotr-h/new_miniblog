from django.urls import path
from . import views

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('<username>/', views.author_detail, name='author_detail'),
  path('', views.author_list, name='author_list'),
  path('<username>/panel/', views.user_panel, name='user_panel'),
  path('<username>/panel/bio_edit/', views.bio_edit, name='bio_edit'),
]