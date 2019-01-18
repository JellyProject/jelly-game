from django.urls import path

from . import rules_tests
from . import atests
# from . import tests

from . import views

urlpatterns = [
    # urls de test vv (a supprimer)
    path('test_player', atests.test_player_model, name='test_player'),
    path('test_game', atests.test_game_model, name='test_game'),
    path('test_rules', rules_tests.test_rules, name='test_rules'),
    # path('test_player', tests.test_player_model, name='test_player'),
    # path('test_game', tests.test_game_model, name='test_game'),
    # path('test_buildings', tests.test_buildings_model, name='test_buildings'),

    # ----- API URLs ----- #
    # Balance model
    path('balance/', views.ListBalance.as_view()),
    path('balance/<int:pk>/', views.DetailBalance.as_view()),

    # Building model
    path('building/', views.ListBuilding.as_view()),
    path('building/<int:pk>/', views.DetailBuilding.as_view()),

    # Event model
    path('event/', views.ListEvent.as_view()),
    path('event/<int:pk>/', views.DetailEvent.as_view()),

    # Game model
    path('game/', views.ListGame.as_view()),
    path('game/<int:pk>/', views.DetailGame.as_view()),

    # HydrocarbonSupplyPile model
    path('hydrocarbon_supply_pile/', views.ListHydrocarbonSupplyPile.as_view()),
    path('hydrocarbon_supply_pile/<int:pk>/', views.DetailHydrocarbonSupplyPile.as_view()),

    # Player model
    path('player/', views.ListPlayer.as_view()),
    path('player/<int:pk>/', views.DetailPlayer.as_view()),

    # Production model
    path('production/', views.ListProduction.as_view()),
    path('production/<int:pk>/', views.DetailProduction.as_view()),

    # Profile model
    path('profile/', views.ListProfile.as_view()),
    path('profile/<int:pk>/', views.DetailProfile.as_view()),

    # Resources model
    path('resources/', views.ListResources.as_view()),
    path('resources/<int:pk>/', views.DetailResources.as_view()),

    # SourceBuilding model
    path('source_building/', views.ListSourceBuilding.as_view()),
    path('source_building/<int:pk>/', views.DetailSourceBuilding.as_view()),

    # SourceEvent model
    path('source_event/', views.ListSourceEvent.as_view()),
    path('source_event/<int:pk>/', views.DetailSourceEvent.as_view()),

    # SourceTechnology model
    path('source_technology/', views.ListSourceTechnology.as_view()),
    path('source_technology/<int:pk>/', views.DetailSourceTechnology.as_view()),

    # Technology model
    path('technology/', views.ListTechnology.as_view()),
    path('technology/<int:pk>/', views.DetailTechnology.as_view()),

    # vraies urls vv
    # y en a pas encore ...
    # il ne devrait pas y en avoir !!
]
