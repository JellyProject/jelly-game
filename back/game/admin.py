from django.contrib import admin
from .models import Game, Player, Resources, Production, HydrocarbonSupplyPile, Balance

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Balance)
admin.site.register(Resources)
admin.site.register(Production)
admin.site.register(HydrocarbonSupplyPile)
# a completer...
