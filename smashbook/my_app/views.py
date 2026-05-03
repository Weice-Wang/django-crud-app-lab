from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player
from .forms import MatchForm




def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def player_index(request):
    players = Player.objects.all()
    return render(request, 'players/index.html', {'players': players})

def player_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    match_form = MatchForm()
    return render(request, 'players/detail.html', {'player': player, 'match_form': match_form})

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__' 


class PlayerUpdate(UpdateView):
    model = Player
    fields = ['gender','racquet','play_style', 'strength', 'weakness', 'utr_rating']

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'

def add_match(request, player_id):
    form = MatchForm(request.POST)
    if form.is_valid():
        new_match = form.save(commit=False)
        new_match.player_id = player_id
        new_match.save()
    return redirect('player-detail', player_id=player_id)