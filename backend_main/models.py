from email.policy import default
from os import name
from django.db import models

# Create your models here.

# TODO character model
class Player(models.Model):
    name = models.CharField(max_length=64)
    health = models.IntegerField(default=100)
    damage = models.IntegerField(default=1)
    inventory = []
    left_hand = ""
    right_hand = ""

    def __str__(self):
        return self.name

# TODO monster model
class Monster(models.Model):
    name = models.CharField(max_length=64)
    health = models.IntegerField(default=50)
    damage = models.IntegerField(default=10)

    def __str__(self):
        return self.name

# TODO weapons model
class Weapon(models.Model):
    type = models.CharField(max_length=64)
    damage = models.IntegerField(default=10)

    def __str__(self):
        return self.type

# TODO item model
class Item(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Map(models.Model):
    name = models.CharField(max_length=64)
    layout = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name