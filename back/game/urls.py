from django.urls import path
from . import views

# API endpoints.
urlpatterns = [
    # SourceTechnology
    path(
         'source-technologies/',
         views.SourceTechnologyList.as_view(),
         name='source-technology-list'
    ),
    path(
         'source-technologies/<slug:version>/',
         views.SourceTechnologyVersionList.as_view(),
         name='source-technology-version-list'
    ),
    path(
         'source-technologies/<slug:version>/<slug:slug>',
         views.SourceTechnologyVersionDetail.as_view(),
         name='source-technology-version-detail'
    ),
    # SourceBuilding
    path(
         'source-buildings/',
         views.SourceBuildingList.as_view(),
         name='source-building-list',
    ),
    path(
         'source-buildings/<slug:version>/',
         views.SourceBuildingVersionList.as_view(),
         name='source-building-version-list'
    ),
    path(
         'source-buildings/<slug:version>/<slug:slug>',
         views.SourceBuildingVersionDetail.as_view(),
         name='source-building-version-detail'
    ),
    # Game
    path(
         'games/',
         views.GameList.as_view(),
         name='game-list'
    ),
    path(
         'games/<int:pk>',
         views.GameDetail.as_view(),
         name='game-detail'
    ),
    # Player
    path(
         'players/',
         views.PlayerList.as_view(),
         name='player-list'
    ),
    path(
         'players/<int:pk>',
         views.PlayerDetail.as_view(),
         name='player-detail'
    ),
    # Building
    path(
         'players/<int:player_pk>/buildings/',
         views.BuildingList.as_view(),
         name='building-list'
    ),
    path(
         'players/<int:player_pk>/buildings/<slug:slug>',
         views.BuildingDetail.as_view(),
         name='building-detail'
    ),
    # Technology
    path(
         'players/<int:player_pk>/technologies/',
         views.TechnologyList.as_view(),
         name='technology-list'
    ),
    path(
         'players/<int:player_pk>/technologies/<slug:slug>',
         views.TechnologyDetail.as_view(),
         name='technology-detail'
    ),
]
