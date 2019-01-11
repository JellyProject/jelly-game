from django.db import models

from .. import game_settings as constant

from .source_building import SourceBuilding


class Building(models.Model):
    """
    Building model

    Fields :
        player (ForeignKey -> Player) : The player who may own this technology.
        index (int) : A unique index to link self to its source copy.
        unlocked (bool) : True -> The player has purchased the required technologies.
        copies (int) : Number of copies of self the player possesses.
    """
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='buildings')
    index = models.IntegerField(editable=False)
    unlocked = models.BooleanField(default=False)
    copies = models.IntegerField(default=0)

    def __str__(self):
        return self.player.profile.user.username + " - " + self.source().name

    def source(self):
        return SourceBuilding.objects.get(pk=self.index, version=self.player.game.version)

    def is_purchasable(self):
        """
            Return the tuple (is_purchasable, error_message).
            error_message will be left empty if is_purchasable is true.
        """
        source = self.source()
        # Era check
        if self.player.game.era < source.era:
            return (False, "Ère trop précoce.")
        # Parent technology check
        if not self.unlocked:
            return (False, "Technologie(s) nécessaire(s)")
        # Cost check
        if source.cost > self.player.resources.money:
            return (False, "Fonds insuffisants.")
        return (True, "")

    def purchase(self):
        """ Grant player a copy of self. """
        source = self.source()

        # Add a copy.
        self.copies += 1

        # Spend money.
        self.player.resources.money -= source.cost
        self.player.resources.save()

        # Apply all modifiers.
        self.player.production.money += source.money_modifier
        self.player.production.food += source.food_modifier
        self.player.production.hydrocarbon += source.hydrocarbon_modifier
        self.player.production.electricity += source.electricity_modifier
        self.player.production.pollution += source.pollution_modifier
        self.player.production.waste += source.waste_modifier
        self.player.production.save()
        self.player.balance.economic += source.economic_modifier
        self.player.balance.social += source.social_modifier
        self.player.balance.environmental += source.environmental_modifier
        self.player.balance.save()

        # Execute self special effect.
        source.execute_special_effect()

