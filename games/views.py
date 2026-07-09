from django.shortcuts import render

from  games.models import Genre, Game

def index(request):
    context = {
        'objects_list': Genre.objects.all()[:3],
        'title': 'Главная страница'
    }
    return  render(request, 'games/index.html', context)