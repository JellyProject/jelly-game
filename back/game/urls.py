from django.urls import path
from . import views
from . import tests

urlpatterns = [
    # urls de test vv
    path('test1', tests.view_game),
    path('test2', tests.test_game_model),

    # vraies urls vv
    # y en a pas encore ...
]
