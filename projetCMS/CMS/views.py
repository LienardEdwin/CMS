from django.shortcuts import render
from .models import Post

def view_posts(request):

    posts = Post.objects.all()


    return render(request, 'index.html', {
        'posts': posts,


    })
