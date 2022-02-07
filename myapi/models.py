from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=60)
    region = models.CharField(max_length=60)

    def __str__(self):
        return self.name
