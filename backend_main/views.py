from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Player, Monster, Weapon, Item, Map
from .serializers import PlayerSerializer, MonsterSerializer, WeaponSerializer, ItemSerializer, MapSerializer

# Player
class PlayerList(ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

# Monster
class MonsterList(ListCreateAPIView):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer

class MonsterDetail(RetrieveUpdateDestroyAPIView):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer

# Weapon
class WeaponList(ListCreateAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

class WeaponDetail(RetrieveUpdateDestroyAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

# Item
class ItemList(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Map
class MapList(ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

class MapDetail(RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer