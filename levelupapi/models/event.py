from django.db import models
from levelupapi.models.gamer import Gamer
from levelupapi.models.game import Game
from datetime import date

class Event(models.Model):
    description = models.CharField(max_length=150,default="")
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE,)
    date = models.DateField()
    time = models.TimeField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE,)
    attendees = models.ManyToManyField("Gamer", through="EventGamer", related_name="attending")

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
            self.__joined = value