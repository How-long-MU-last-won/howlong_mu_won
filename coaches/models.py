import datetime
from django.db import models


# Create your models here.
class Coach(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(blank=True, null=True)
    numTrophies = models.IntegerField(default=0)
    numWins = models.IntegerField(default=0)
    numLosses = models.IntegerField(default=0)
    numTies = models.IntegerField(default=0)
    leadFrom = models.DateField()
    leadTo = models.DateField(blank=True, null=True, default=datetime.date.today)
    moneySpent = models.IntegerField(default=0)
    statURL = models.CharField(max_length=200, blank=True, null=True)

    def totalGames(self):
        return self.numWins + self.numLosses + self.numTies

    def winrate(self):
        return self.numWins / self.totalGames()

    def __str__(self):
        return self.name
