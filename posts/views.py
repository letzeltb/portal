from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Posts
from .forms import NameForm

def test(request):
    return render(request,'posts/test.html')

def index(request):

    posts = Posts.objects.all()[:10]

    context = {
        'Player_Name': 'Player Name',
        'posts': posts
    }

    return render(request,'posts/index.html', context)

def navbar(request):
    return render(request,'posts/navbar.html')

def nav(request,id):

    posts = Posts.objects.get(id=id)

    context = {
        'Player_Name': 'Player Name',
        'posts': posts
    }
    return render(request,'posts/nav.html', context)

def createpost(request):
        if request.method == 'POST':
            if request.POST.get('Player_Name'):
                post=Posts()
                post.Player_Name= request.POST.get('Player_Name')
                post.save()
                
                return render(request, 'posts/navbar.html')  

        else:
                return render(request,'posts/navbar.html')


# def home(request):
#     response = requests.get('http://freegeoip.net/json/')
#     geodata = response.json()
#     return render(request, 'navbar.html', {
#         'ip': geodata['ip'],
#         'country': geodata['country_name']
#     })                
