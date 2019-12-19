from django.db import models


# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Team(models.Model):
    name = models.CharField(max_length=75)
    members = models.ManyToManyField(Player, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def __str__(self):
        return f'{self.player} - {self.team}'
