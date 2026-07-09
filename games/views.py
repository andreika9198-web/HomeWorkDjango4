from django.shortcuts import render

from  games.models import Genre, Game

def index(request):
    context = {
        'objects_list': Genre.objects.all()[:3],
        'title': 'Главная страница'
    }
    return  render(request, 'games/index.html', context)

def genres_list(request):
    context = {
        'objects_list': Genre.objects.all()[:3],
        'title': 'Игры - Список жанров'
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