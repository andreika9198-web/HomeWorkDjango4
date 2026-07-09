from django.db import models

from users.models import  NULLABLE

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='genre')
    description = models.CharField(max_length=1000, verbose_name='description', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

class Game(models.Model):
    name = models.CharField(max_length=250, verbose_name='game_name')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='genre')
    photo = models.ImageField(upload_to='games/', **NULLABLE, verbose_name='photo')
    date_of_publication = models.DateField(**NULLABLE, verbose_name='date_of_publication')

    def __str__(self):
        return f'{self.name} ({self.genre})'

    class Meta:
        verbose_name = 'game'
        verbose_name_plural = 'games'
