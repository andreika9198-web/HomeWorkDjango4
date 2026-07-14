from django import forms

from games.models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__' #(те поля которые есть в модели)
        # exclude = (те поля которые есть в модели)
        