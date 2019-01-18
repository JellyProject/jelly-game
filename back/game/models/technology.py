from django.db import models

from .. import game_settings as constant


class Technology(models.Model):
    """
    Technology model

    Fields :
        player (ForeignKey -> Player) : The player who may own this technology.
        index (int) : A unique index to link this technology to a source technology.
        unlocked (bool) : True -> This technology may be purchased by the player.
        purchased (bool) : True -> This technology has been purchased by the player.
    """
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='technologies', editable=False)
    index = models.IntegerField(unique=True, editable=False)
    unlocked = models.BooleanField(default=False)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return "{0} (Game : {1}, Player : {2})".format(self.source().name,
                                                       self.player.game.name,
                                                       self.player.username())

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __eq__(self, other):
        return (self.player.id == other.player.id and
                self.index == other.index and
                self.unlocked == other.unlocked and
                self.purchased == other.purchased)

    def source(self):
        return self.player.game.source_technologies.get(pk=self.index)

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
        # Has been purchased check
        if self.purchased == True:
            return (False, "Technologie déjà acquise.")
        return (True, "")

    def purchase(self):
        """ Grant player a copy of self. """
        source = self.source()

        # Purchase the technology.
        self.purchased = True
        self.save()

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

        # Unlock child technology
        try:
            child_tech_sources = self.source().child_technologies.all()
            for child_tech_source in child_tech_sources:
                child_tech = self.player.technologies.get(index=child_tech_source.pk)
                child_tech.unlocked = True
                child_tech.save()
        except:
            pass

        # Unlock child building
        try:
            child_build_source = self.source().child_building
            child_build = self.player.buildings.get(index=child_build_source.pk)
            child_build.unlocked = True
            child_build.save()
        except:
            pass

        # Execute self special effect.
        source.execute_special_effect()