from django.urls import path
from . import views

# API endpoints.
urlpatterns = [
    # SourceTechnology
    path('api/source-technologies', views.SourceTechnologyList.as_view()),
    path('api/source-technologies/<slug:version>', views.SourceTechnologyVersionList.as_view()),
    path('api/source-technologies/<slug:version>/<slug:slug>', views.SourceTechnologyVersionDetail.as_view()),
    # SourceBuilding
    path('api/source-buildings', views.SourceBuildingList.as_view()),
    path('api/source-buildings/<slug:version>', views.SourceBuildingVersionList.as_view()),
    path('api/source-buildings/<slug:version>/<slug:slug>', views.SourceBuildingVersionDetail.as_view()),
    # Game
    path('api/games', views.GameList.as_view()),
    path('api/games/<int:pk>', views.GameDetail.as_view()),
    # Profile
    path('api/profiles', views.ProfileList.as_view()),
    path('api/profiles/<slug:username>', views.ProfileDetail.as_view()),
    # Player
    path('api/players/', views.PlayerList.as_view()),
    path('api/players/<int:pk>', views.PlayerDetail.as_view()),
    # Building
    path('api/players/<int:player_pk>/buildings', views.BuildingList.as_view()),
    path('api/players/<int:player_pk>/buildings/<slug:slug>', views.BuildingDetail.as_view()),
    # Technology
    path('api/players/<int:player_pk>/technologies', views.TechnologyList.as_view()),
    path('api/players/<int:player_pk>/technologies/<slug:slug>', views.TechnologyDetail.as_view()),
]
