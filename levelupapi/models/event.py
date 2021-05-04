from django.db import models
from levelupapi.models.gamer import Gamer
from levelupapi.models.game import Game
from datetime import date

class Event(models.Model):
    description = models.CharField(max_length=150,default="")
    event_date = models.DateField(default=date.today)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE,)
    game = models.ForeignKey("Game", on_delete=models.CASCADE,)
    attendees = models.ManyToManyField("Gamer", through="EventGamer", related_name="attending")
