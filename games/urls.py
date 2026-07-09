from  django.urls import path


from  games.views import  index
from  games.apps import  GamesConfig

app_name = GamesConfig.name

urlpatterns = [
    path('', index, name='index'),
]