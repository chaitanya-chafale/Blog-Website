from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('posts/<str:post_id>', views.posts, name = 'posts')
]