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
    slug = models.CharField(max_length=40, default='fire-discovery', editable=False)
    unlocked = models.BooleanField(default=False)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return "{0} (Game : {1}, Player : {2})".format(self.source().name,
                                                       self.player.game.pk,
                                                       self.player.username())

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __eq__(self, other):
        return (self.player.id == other.player.id and
                self.slug == other.slug and
                self.unlocked == other.unlocked and
                self.purchased == other.purchased)

    def source(self):
        return self.player.game.source_technologies.get(slug=self.slug)

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

    def trigger_post_purchase_effects(self):
        """
        Update player statistics after self purchase.
        WARNING : the actual purchase should be done in a separate function.
        """
        # Load self source_technology
        source = self.source()

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

        # Unlock child technologies
        try:
            for child_tech_source in source.child_technologies.all():
                child_tech = self.player.technologies.get(slug=child_tech_source.slug).unlocked = True
                child_tech.unlocked = True
                child_tech.save()
        except:
            pass

        # Unlock child building
        try:
            child_build_source = self.source().child_building
            child_build = self.player.buildings.get(slug=child_build_source.slug)
            child_build.unlocked = True
            child_build.save()
        except:
            pass

        # Execute self special effect.
        source.execute_special_effect()