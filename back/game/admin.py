from django.contrib import admin
from .models import Player, Resources, Production, HydrocarbonSupplyPile, States

admin.site.register(Player)
admin.site.register(States)
admin.site.register(Resources)
admin.site.register(Production)
admin.site.register(HydrocarbonSupplyPile)
