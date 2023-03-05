from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import BlogPost, Comment
from .forms import EntryForm, CommentForm


def index(request):
    '''The home page for the blog'''
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


def view_post(request, post_id):
    '''View a blog post.'''
    try:
        post = BlogPost.objects.get(id=post_id)
        comments = post.comment_set.order_by('date_added')
    except ObjectDoesNotExist as DoesNotExist:
        raise Http404
    context = {'post': post, 'comments': comments}
    return render(request, 'blogs/view_post.html', context)


def create_post(request):
    '''Add a new post.'''
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/create_post.html', context)


def edit_post(request, post_id):
    '''Edit an existing blog post'''
    try:
        post = BlogPost.objects.get(id=post_id)
    except ObjectDoesNotExist as DoesNotExist:
        raise Http404

    if request.method != 'POST':
        # Initialize and pre-fill form with blog post.
        form = EntryForm(instance=post)
    else:
        form = EntryForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:view_post', post_id=post.id)

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)


def add_comment(request, post_id):
    '''Add a new comment on a blog post.'''
    post = BlogPost.objects.get(id=post_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blogs:view_post', post_id=post_id)
    # Display a blank or invalid form
    context = {'post': post, 'form': form}
    return render(request, 'blogs/add_comment.html', context)


def edit_comment(request, post_id, comment_id):
    '''Edit an existing comment'''
    try:
        comment = Comment.objects.get(id=comment_id)
        post = comment.post
    except ObjectDoesNotExist as DoesNotExist:
        raise Http404

    if request.method != 'POST':
        # Initialize and pre-fill form with blog post.
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:view_post', post_id=post.id)

    context = {'comment': comment, 'post': post, 'form': form}
    return render(request, 'blogs/edit_comment.html', context)
