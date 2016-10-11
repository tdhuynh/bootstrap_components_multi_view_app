from django.db import models


class Faction(models.Model):
    side = models.CharField(max_length=6)
    name = models.CharField(max_length=50)
    play_style = models.TextField()

    def __str__(self):
        return self.name
