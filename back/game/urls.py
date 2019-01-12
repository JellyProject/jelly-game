from django.urls import path
from . import views
from . import rules_tests
from . import atests
# from . import tests

urlpatterns = [
    # urls de test vv
    path('test_player', atests.test_player_model, name='test_player'),
    path('test_game', atests.test_game_model, name='test_game'),
    path('test_rules', rules_tests.test_rules, name='test_rules'),
    # path('test_player', tests.test_player_model, name='test_player'),
    # path('test_game', tests.test_game_model, name='test_game'),
    # path('test_buildings', tests.test_buildings_model, name='test_buildings'),

    # API
    path('', views.ListGame.as_view()),
    path('<int:pk>/', views.DetailGame.as_view()),

    # vraies urls vv
    # y en a pas encore ...
]
