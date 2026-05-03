from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player
from .forms import MatchForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin





class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')

@login_required
def player_index(request):
    players = Player.objects.filter(user=request.user)
    return render(request, 'players/index.html', {'players': players})

def player_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    match_form = MatchForm()
    return render(request, 'players/detail.html', {'player': player, 'match_form': match_form})

class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = '__all__' 

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model = Player
    fields = ['gender','racquet','play_style', 'strength', 'weakness', 'utr_rating']

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'

@login_required
def add_match(request, player_id):
    form = MatchForm(request.POST)
    if form.is_valid():
        new_match = form.save(commit=False)
        new_match.player_id = player_id
        new_match.save()
    return redirect('player-detail', player_id=player_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('player-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
   