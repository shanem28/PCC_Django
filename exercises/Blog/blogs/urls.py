from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('edit/<int:post_id>/<int:comment_id>/',
         views.edit_comment, name='edit_comment'),
]
