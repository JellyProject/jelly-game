from django.urls import path
from . import views

# API endpoints.
urlpatterns = [
    # SourceTechnology
    path('source-technologies/', views.SourceTechnologyList.as_view()),
    path('source-technologies/<slug:version>/', views.SourceTechnologyVersionList.as_view()),
    path('source-technologies/<slug:version>/<slug:slug>', views.SourceTechnologyVersionDetail.as_view()),
    # SourceBuilding
    path('source-buildings/', views.SourceBuildingList.as_view()),
    path('source-buildings/<slug:version>/', views.SourceBuildingVersionList.as_view()),
    path('source-buildings/<slug:version>/<slug:slug>', views.SourceBuildingVersionDetail.as_view()),
    # Game
    path('games/', views.GameList.as_view()),
    path('games/<int:pk>', views.GameDetail.as_view()),
    # Profile
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<slug:username>', views.ProfileDetail.as_view()),
    # Player
    path('players/', views.PlayerList.as_view()),
    path('players/<int:pk>', views.PlayerDetail.as_view()),
    # Building
    path('players/<int:player_pk>/buildings/', views.BuildingList.as_view()),
    path('players/<int:player_pk>/buildings/<slug:slug>', views.BuildingDetail.as_view()),
    # Technology
    path('players/<int:player_pk>/technologies/', views.TechnologyList.as_view()),
    path('players/<int:player_pk>/technologies/<slug:slug>', views.TechnologyDetail.as_view()),
]
