from django.shortcuts import render
from .models import Cat

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def game_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', { 'games': games })
