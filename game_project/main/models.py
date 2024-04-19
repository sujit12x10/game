from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Season(models.Model):
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    editon = models.CharField(max_length=4)
    teams = models.IntegerField()
    matches = models.IntegerField()
    winner = models.ForeignKey(Team, blank=True, null=True, related_name='season_wins', on_delete=models.CASCADE)
    runnerup = models.ForeignKey(Team, blank=True, null=True, related_name='runnerup',on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.editon

class Match(models.Model):
    season = models.ForeignKey(Season, related_name='mathe', on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, blank=True, null=True, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, blank=True, null=True, related_name='team2', on_delete=models.CASCADE)
    discription = models.CharField(max_length=100, default='league-match')
    winner = models.ForeignKey(Team, blank=True, null=True, related_name='winner', on_delete=models.CASCADE)
    loser = models.ForeignKey(Team, blank=True, null=True, related_name='loser', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.team1) + ' vs ' + str(self.team2)
    
class PointsTable(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='points_table')

    def __str__(self):
        return str(self.season)
    

