import datetime
from django.db import models

from trophies.models import Trophy


# Create your models here.
class Coach(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(blank=True, null=True)
    numWins = models.IntegerField(default=0)
    numLosses = models.IntegerField(default=0)
    numTies = models.IntegerField(default=0)
    leadFrom = models.DateField()
    leadTo = models.DateField(blank=True, null=True, default=datetime.date.today)
    moneySpent = models.IntegerField(default=0)
    statURL = models.CharField(max_length=200, blank=True, null=True)
    shortDesc = models.TextField(blank=True, null=True)
    numPlayersUsed = models.IntegerField(default=0)
    trophyWon = models.ManyToManyField(Trophy, related_name="trophyWon", blank=True)

    def totalGames(self):
        return self.numWins + self.numLosses + self.numTies

    def winrate(self):
        return self.numWins / self.totalGames()

    def __str__(self):
        return self.name
