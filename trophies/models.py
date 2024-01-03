from django.db import models
from coaches.models import Coach

# Create your models here.


class Trophy(models.Model):
    name = models.CharField(max_length=100)
    lastWonDate = models.DateField()
    numTimesWon = models.IntegerField()
    lastWonBy = models.ForeignKey(
        Coach, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name
