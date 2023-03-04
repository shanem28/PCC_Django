from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import BlogPost
from .forms import EntryForm


def index(request):
    '''The home page for the blog'''
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


def view_post(request, post_id):
    '''View a blog post.'''
    try:
        post = BlogPost.objects.get(id=post_id)
    except ObjectDoesNotExist as DoesNotExist:
        raise Http404
    context = {'post': post}
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
