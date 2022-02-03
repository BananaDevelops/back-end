from django.urls import path
from .views import (
    PlayerList, PlayerDetail, 
    MonsterList, MonsterDetail, 
    WeaponList, WeaponDetail, 
    ItemList, ItemDetail,
    MapDetail, MapList,
    PromptList, PromptDetail,
)

urlpatterns = [
    path("player/", PlayerList.as_view(), name="player_list"),
    path("player/<int:pk>/", PlayerDetail.as_view(), name="player_detail"),
    path("monster/", MonsterList.as_view(), name="monster_list"),
    path("monster/<int:pk>/", MonsterDetail.as_view(), name="monster_detail"),
    path("weapon/", WeaponList.as_view(), name="weapon_list"),
    path("weapon/<int:pk>/", WeaponDetail.as_view(), name="weapon_detail"),
    path("item/", ItemList.as_view(), name="item_list"),
    path("item/<int:pk>/", ItemDetail.as_view(), name="item_detail"),
    path("map/", MapList.as_view(), name="map_list"),
    path("map/<int:pk>/", MapDetail.as_view(), name="map_detail"),
    path("prompt/", PromptList.as_view(), name="map_list"),
    path("prompt/<int:pk>/", PromptDetail.as_view(), name="map_detail"),
]
