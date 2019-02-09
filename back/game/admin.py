from django.contrib import admin
from .models import SourceBuilding, SourceEvent, SourceTechnology
from .models import Game, Event, HydrocarbonSupplyPile
from .models import Profile
from .models import Player, ShadowPlayer, PlayerState, Balance, Building, Production, Resources, Technology

admin.site.register(SourceBuilding)
admin.site.register(SourceEvent)
admin.site.register(SourceTechnology)
admin.site.register(Game)
admin.site.register(Event)
admin.site.register(HydrocarbonSupplyPile)
admin.site.register(Profile)
admin.site.register(Player)
admin.site.register(ShadowPlayer)
admin.site.register(PlayerState)
admin.site.register(Balance)
admin.site.register(Building)
admin.site.register(Production)
admin.site.register(Resources)
admin.site.register(Technology)
# To be continued...
