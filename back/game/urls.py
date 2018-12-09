from django.urls import path
from . import views
from . import tests

urlpatterns = [
    # urls de test vv
    path('test_player', tests.test_player_model, name='test_player'),
    path('test_game', tests.test_game_model, name='test_game'),
    path('test_buildings', tests.test_buildings_model, name='test_buildings'),

    # vraies urls vv
    # y en a pas encore ...
]
