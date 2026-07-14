from django.shortcuts import render
from django.http import  HttpResponseRedirect
from  django.urls import reverse

from  games.models import Genre, Game
from  games.forms import GameForm

def index(request):
    context = {
        'objects_list': Genre.objects.all()[:3],
        'title': 'Главная страница'
    }
    return  render(request, 'games/index.html', context)

def genres_list(request):
    context = {
        'objects_list': Genre.objects.all()[:3],
        'title': 'Список жанров игр'
    }
    return render(request, 'games/genres.html', context)

def genres_games_list(request, pk: int):
    genre_item = Genre.objects.get(pk=pk)
    context = {
        'objects_list': Game.objects.filter(genre_id=pk),
        'title': f'Жанр игры  - {genre_item}',
        'breed_pk': genre_item.pk
    }
    return render(request, 'games/games.html', context)

def games_list_view(request):
    context = {
        'objects_list': Game.objects.all(),
        'title': f'Все игры',
    }
    return render(request, 'games/games.html', context)

def game_create_view(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('games:games_list'))
    context = {
        'title': 'Добавить игру',
        'form': GameForm()
    }
    return render(request, 'games/create.html', context)

