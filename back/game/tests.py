from django.test import TestCase
# faudrait regerder ce que c'est ^^
# oui c'est vrai

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime
from game.models import Game, Player, HydrocarbonSupplyPile, Resources, Production, States, User


def test_player_model(request):

    user1 = User(
        name='Miguel de Patatas',
        email='a@a.com')

    player = Player(
        resources=Resources(),
        production=Production(),
        states=States(),
        user=user1)
    # green_income = player.green_income()
    return render(request, 'back/test_player.html', locals())


def test_game_model(request):
    game, game_created = Game.objects.get_or_create(name='game4')

    user1, user_created = User.objects.get_or_create(
        name='Miguel de Patatas',
        email='a@a.com')

    if game_created:
        game._init_supply()
    game.add_player(user1)
    game.income_phase()
    player = game.players.get(user__name='Miguel de Patatas')
    # green_income = player.green_income()
    stock0 = game.hydrocarbon_piles.get(index=0).stock_amount
    stock1 = game.hydrocarbon_piles.get(index=1).stock_amount
    stock2 = game.hydrocarbon_piles.get(index=2).stock_amount
    return render(request, 'back/test_game.html', locals())
