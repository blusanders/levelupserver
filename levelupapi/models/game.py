from django.db import models
from levelupapi.models.game_type import GameType
from levelupapi.models.gamer import Gamer

class Game(models.Model):
    title = models.CharField(max_length=55)
    maker = models.CharField(max_length=55, default="")
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE, default=0)
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE,)
    number_of_players = models.IntegerField(default=1)
    skill_level = models.IntegerField(default=1)
