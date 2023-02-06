from django.db import models


class Teams(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    coach = models.CharField(max_length=200)
    captain = models.CharField(max_length=200)
    set_of_players = models.IntegerField(max_length=50)
    # pub_date = models.DateTimeField('date published')


class Players(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    skill_level = models.IntegerField(max_length=10)
    set_of_injury = models.IntegerField(max_length=100)


class Game(models.Model):
    host_team = models.CharField(max_length=50)
    guest_team = models.CharField(max_length=50)
    date = models.DateTimeField('date published')
    host_score = models.IntegerField(max_length=100)
    guest_score = models.IntegerField(max_length=100)


