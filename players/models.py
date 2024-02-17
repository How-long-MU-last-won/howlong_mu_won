from django.db import models
from coaches.models import Coach


# Create your models here.
class Position(models.Model):
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.position


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    numGamesPlayed = models.IntegerField()
    playFrom = models.DateField()
    playTo = models.DateField(null=True, blank=True)
    statURL = models.CharField(max_length=200, null=True)
    boughtBy = models.ForeignKey(
        Coach, on_delete=models.CASCADE, null=True, related_name="boughtBy"
    )
    workWith = models.ManyToManyField(
        Coach, related_name="workWith", null=True, blank=True
    )
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
