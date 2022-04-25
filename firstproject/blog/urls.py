from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='blog-home'),
    path('about',views.you, name='blog-about'),
    path('what',views.new, name='blog-contactUs'),
    # path('post/new',views.post_new, name='post_new'),
    path('read-post/<int:pk>',views.readpost, name='read-post'),
    path('update-post/<int:pk>',views.updatepost, name='update-post'),
    path('delete-post/<int:pk>',views.deletepost, name='delete-post'),
    path('create-post',views.CreateNewPost, name='create-post'),
]