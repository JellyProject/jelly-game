from django.test import TestCase  # faudrait regerder ce que c'est

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime

import game.models as models
from game.models import Game, Player, HydrocarbonSupplyPile, Resources, Production, States


# Create your views here.
def view_game(request):
    players = models.Player.objects.all()
    player = models.Player(name='Miguel de Patatas', resources=models.Resources(), production=models.Production(),
                           states=models.States())
    green_income = player.green_income()
    return render(request, 'back/test.html', locals())


def test_game_model(request):
    game = Game.objects.get_or_create(name="AAA")[0]
    game.new_player("Miguel")
    player = game.players[0]
    green_income = player.green_income()
    return render(request, 'back/test.html', locals())


def test():
    game = Game.objects.get_or_create(name='aa')[0]
    game.new_player('Miguela')
