from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/new/', views.create_post, name='blog-create'),
]

