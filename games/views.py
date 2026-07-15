from django.shortcuts import render, get_object_or_404
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
    return render(request, 'games/create_update.html', context)

def game_detail_view(request, pk):
    game_object = get_object_or_404(Game, pk=pk)
    context = {
        'object': game_object,
        'title': f'Вы выбрали {game_object}',
    }
    return  render(request, 'games/detail.html', context)

def game_update_view(request, pk):
    game_object = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game_object)
        if form.is_valid():
            game_object = form.save()
            game_object.save()
            return HttpResponseRedirect(reverse('games:game_detail', args={pk:pk}))
    context = {
        'title': 'Изменить игру',
        'object': game_object,
        'form': GameForm(instance=game_object)
    }
    return render(request, 'games/create_update.html', context)


def game_delete_view(request, pk):
    game_object = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        game_object.delete()
        return HttpResponseRedirect(reverse('games:games_list'))
    context =  {
        'title': 'Удалить игру',
        'object': game_object,
    }
    return render(request, 'games/delete.html', context)