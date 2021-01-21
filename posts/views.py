from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

def test(request):
    return render(request,'posts/test.html')

def index(request):

    posts = Posts.objects.all()[:10]

    context = {
        'Player_Name': 'Player Name',
        'posts': posts
    }

    return render(request,'posts/index.html', context)


def nav(request,id):

    posts = Posts.objects.get(id=id)

    context = {
        'Player_Name': 'Player Name',
        'posts': posts
    }
    return render(request,'posts/nav.html', context)

