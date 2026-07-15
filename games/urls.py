from  django.urls import path


from  games.views import  (index, genres_list, genres_games_list, games_list_view,
                           game_create_view,game_detail_view, game_update_view)
from  games.apps import  GamesConfig

app_name = GamesConfig.name

urlpatterns = [
    path('', index, name='index'),
    # genres
    path('genres/', genres_list, name='genres'),
    path('genres/<int:pk>/games/', genres_games_list, name='genres_games'),

    # games
    path('games/', games_list_view, name='games_list'),
    path('games/create/', game_create_view, name='game_create'),
    path('games/detail/<int:pk>/', game_detail_view, name='game_detail'),
path('games/update/<int:pk>/', game_update_view, name='game_update'),
]