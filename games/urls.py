from  django.urls import path


from  games.views import  index, genres_list, genres_games_list, games_list_view
from  games.apps import  GamesConfig

app_name = GamesConfig.name

urlpatterns = [
    path('', index, name='index'),
    # genres
    path('genres/', genres_list, name='genres'),
    path('genres/<int:pk>/games/', genres_games_list, name='genres_games'),

    # games
    path('games/', games_list_view, name='games_list')
]