from django.shortcuts import render_to_response
from .models import Post

def view_posts(request):

    posts = Post.objects.all()
    return render_to_response('index.html', {
        'posts': posts,

    })