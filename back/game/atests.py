from django.test import TestCase
# faudrait regerder ce que c'est ^^
# oui c'est vrai

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Game, Player, HydrocarbonSupplyPile, Resources, Production, Balance, Profile, Building, \
    PlayerBuilding
from django.contrib.auth.models import User
from django.contrib.auth import get_user


def test_player_model(request):

    try:
        user1 = User.objects.create_user(username='Miguel', email='a@a.com', password='sup3rp@ssw0rd')
    except:
        user1 = User.objects.get(username='Miguel')
    profile = Profile(user=user1)

    player = Player(
        resources=Resources(),
        production=Production(),
        balance=Balance(),
        profile=profile)
    # green_income = player.green_income()
    return render(request, 'back/test_player.html', locals())


def test_game_model(request):
    game, game_created = Game.objects.get_or_create(name='game5')

    try:
        user1 = User.objects.create_user(username='Miguel de Patatas', email='a@a.com', password='sup3rp@ssw0rd')
    except:
        user1 = User.objects.get(username='Miguel de Patatas')
    profile = Profile.objects.get_or_create(user=user1)[0]

    if game_created:
        game._init_supply()
    game.add_player(profile)
    game.income_phase()
    player = game.players.get(profile__user__username='Miguel de Patatas')

    stock0 = game.hydrocarbon_piles.get(index=0).stock_amount
    stock1 = game.hydrocarbon_piles.get(index=1).stock_amount
    stock2 = game.hydrocarbon_piles.get(index=2).stock_amount
    return render(request, 'back/test_game.html', locals())
