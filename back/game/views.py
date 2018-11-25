from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime

import game.models as models
from game.game import Game


# Create your views here.
def view_game(request):
    players = models.Player.objects.all()
    player = models.Player(name='Miguel de Patatas', resources=models.Resources(), production=models.Production(),
                           states=models.States())
    green_income = player.green_income()
    return render(request, 'back/test.html', locals())
