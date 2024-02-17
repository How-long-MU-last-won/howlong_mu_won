from django.db import models

# Create your models here.


class Trophy(models.Model):
    name = models.CharField(max_length=100)
    lastWonDate = models.DateField()
    numTimesWon = models.IntegerField()

    def __str__(self):
        return self.name
