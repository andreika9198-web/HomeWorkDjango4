from django.contrib import admin

from  games.models import  Genre,Game

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    ordering = ('pk',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'genre',)
    list_filter = ('genre',)
    ordering = ('name',)
