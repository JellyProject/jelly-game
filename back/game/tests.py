from django.test import TestCase
# faudrait regerder ce que c'est ^^
# oui c'est vrai

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime
from game.models import Game, Player, HydrocarbonSupplyPile, Resources, Production, States


def test_player_model(request):
    players = Player.objects.all()
    player = Player(
        name='Miguel de Patatas',
        resources=Resources(),
        production=Production(),
        states=States())
    # green_income = player.green_income()
    return render(request, 'back/test.html', locals())


def test_game_model(request):
    game, created = Game.objects.get_or_create(name='clasa')
    if created:
        game._init_supply()
    game.add_player('Miguel')
    game.income_phase()
    player = game.players.get(name='Miguel')
    # green_income = player.green_income()
    stock0 = game.hydrocarbon_piles.get(index=0).stock_amount
    stock1 = game.hydrocarbon_piles.get(index=1).stock_amount
    stock2 = game.hydrocarbon_piles.get(index=2).stock_amount
    return render(request, 'back/test.html', locals())
