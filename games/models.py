from django.db import models

from users.models import  NULLABLE

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Жанр')
    description = models.CharField(max_length=1000, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

class Game(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название игры')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр')
    photo = models.ImageField(upload_to='games/', **NULLABLE, verbose_name='Фото')
    date_of_publication = models.DateField(**NULLABLE, verbose_name='Дата выхода')

    def __str__(self):
        return f'{self.name} ({self.genre})'

    class Meta:
        verbose_name = 'game'
        verbose_name_plural = 'games'
