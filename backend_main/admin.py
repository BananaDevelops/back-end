from django.contrib import admin
from .models import Player, Monster, Weapon, Item, Map

# Register your models here.
admin.site.register(Player)
admin.site.register(Monster)
admin.site.register(Weapon)
admin.site.register(Item)
admin.site.register(Map)
