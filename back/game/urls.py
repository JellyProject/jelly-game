from django.urls import path
from . import views
from . import atests

urlpatterns = [
    # urls de test vv
    path('test_player', atests.test_player_model, name='test_player'),
    path('test_game', atests.test_game_model, name='test_game'),
    # path('test_buildings', tests.test_buildings_model, name='test_buildings'),

    # vraies urls vv
    # y en a pas encore ...
]
