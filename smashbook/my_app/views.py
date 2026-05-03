from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player




def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def player_index(request):
    players = Player.objects.all()
    return render(request, 'players/index.html', {'players': players})

def player_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    return render(request, 'players/detail.html', {'player': player})

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__' 


class PlayerUpdate(UpdateView):
    model = Player
    fields = ['gender','racquet','play_style', 'strength', 'weakness', 'utr_rating']

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'
