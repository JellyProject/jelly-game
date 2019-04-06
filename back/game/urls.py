from django.urls import path
from . import views

# API endpoints.
urlpatterns = [
    # SourceTechnology
    path(
        'source-technologies/<slug:version>/',
        views.SourceTechnologyList.as_view(),
        name='source-technology-list'
    ),
    path(
        'source-technologies/<slug:version>/<slug:slug>',
        views.SourceTechnologyDetail.as_view(),
        name='source-technology-detail'
    ),
    # SourceBuilding
    path(
        'source-buildings/<slug:version>/',
        views.SourceBuildingList.as_view(),
        name='source-building-list'
    ),
    path(
        'source-buildings/<slug:version>/<slug:slug>',
        views.SourceBuildingDetail.as_view(),
        name='source-building-detail'
    ),
    # Game
    # path(
    #     'games/',
    #     views.GameList.as_view(),
    #     name='game-list'
    # ),
    path(
        'games/<uuid:join_token>/',
        views.GameRetrieveUpdateAPIView.as_view(),
        name='game-retrieve-update'
    ),
    path(
        'games/',
        views.GameCreateAPIView.as_view(),
        name='game-creation'
    ),
    # Player
    # path(
    #     'players/',
    #     views.PlayerList.as_view(),
    #     name='player-list'
    # ),
    path(
        'players/<int:pk>',
        views.PlayerDetail.as_view(),
        name='player-detail'
    ),
    path(
        'players/',
        views.PlayerAddAPIView.as_view(),
        name='player-add'
    ),
    # ShadowPlayer
    path(
        'shadow-players/',
        views.ShadowPlayerList.as_view(),
        name='shadow_player-list'
    ),
    path(
        'shadow-players/<int:pk>',
        views.ShadowPlayerDetail.as_view(),
        name='shadow_player-detail'
    ),
    # PlayerState
    path(
        'player-states/',
        views.PlayerStateList.as_view(),
        name='player_state-list'
    ),
    path(
        'player-states/<int:pk>',
        views.PlayerStateDetail.as_view(),
        name='player_state-detail'
    ),
    # Building
    path(
        'player-states/<int:player_state_pk>/buildings/',
        views.BuildingList.as_view(),
        name='building-list'
    ),
    path(
        'player-states/<int:player_state_pk>/buildings/<slug:source_slug>',
        views.BuildingRetrieveUpdateAPIView.as_view(),
        name='building-detail'
    ),
    # Technology
    path(
        'player-states/<int:player_state_pk>/technologies/',
        views.TechnologyList.as_view(),
        name='technology-list'
    ),
    path(
        'player-states/<int:player_state_pk>/technologies/<slug:source_slug>',
        views.TechnologyRetrieveUpdateAPIView.as_view(),
        name='technology-detail'
    ),
]
