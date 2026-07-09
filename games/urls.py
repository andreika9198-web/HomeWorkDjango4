from  django.urls import path


from  games.views import  index, genres_list, genres_games_list
from  games.apps import  GamesConfig

app_name = GamesConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('genres/', genres_list, name='genres'),
    path('genres/<int:pk>/games/', genres_games_list, name='genres_games'),
]