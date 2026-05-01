from django.shortcuts import render
from django.http import HttpResponse
from .models import Player



def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def player_index(request):
    players = Player.objects.all()
    return render(request, 'players/index.html', {'players': players})