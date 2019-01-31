from django.urls import path
from . import views

# API endpoints.
urlpatterns = [
    # SourceTechnology
    path('api/source-technology/', views.SourceTechnologyList.as_view()),
    path('api/source-technology/<slug:version>/', views.SourceTechnologyVersionList.as_view()),
    path('api/source-technology/<slug:version>/<slug:slug>/', views.SourceTechnologyVersionDetail.as_view()),
    # SourceBuilding
    path('api/source-building/', views.SourceBuildingList.as_view()),
    path('api/source-building/<slug:version>/', views.SourceBuildingVersionList.as_view()),
    path('api/source-building/<slug:version>/<slug:slug>/', views.SourceBuildingVersionDetail.as_view()),
    # Game
    path('api/game/', views.GameList.as_view()),
    path('api/game/<int:pk>/', views.GameDetail.as_view()),
]
