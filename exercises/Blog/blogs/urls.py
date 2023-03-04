from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('create_post/', views.create_post, name='create_post'),
]
