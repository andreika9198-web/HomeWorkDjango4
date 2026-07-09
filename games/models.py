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

