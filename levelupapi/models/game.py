from django.db import models
from levelupapi.models.game_type import GameType

class Game(models.Model):
    title = models.CharField(max_length=55)
    maker = models.CharField(max_length=55)
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE,)
    number_of_players = models.IntegerField(default=1)
    skill_level = models.IntegerField(default=1)
