from email.policy import default
from os import name
import black
from django.db import models

# Create your models here.

# TODO character model
class Player(models.Model):
    name = models.CharField(max_length=64)
    health = models.IntegerField(default=100)
    damage = models.IntegerField(default=1)
    inventory = models.JSONField(default=list, blank=True)
    left_hand = models.JSONField(default=dict, blank=True)
    right_hand = models.JSONField(default=dict, blank=True)

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

# TODO map model
class Map(models.Model):
    name = models.CharField(max_length=64)
    layout = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name

# TODO prompt model
class Prompt(models.Model):
    text = models.TextField(max_length=256)

    def __str__(self):
        return self.text