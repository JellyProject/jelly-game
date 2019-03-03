from django.db import models

from .. import game_settings as constant

from .source_building import SourceBuilding


class Building(models.Model):
    """
    Building model

    Fields :
        * state (OneToOne -> PlayerState) : global state of the player related to the balance
        * unlocked (bool) : True -> The player has purchased the required technologies.
        * copies (int) : Number of copies of self the player possesses.
        * quantity_cap (int) : The maximal number of buildings of this type purchasable
        * source (ForeignKey -> SourceBuilding) : source event corresponding
    """
    state = models.ForeignKey('PlayerState', on_delete=models.CASCADE, related_name='buildings', editable=False)
    unlocked = models.BooleanField(default=False)
    copies = models.IntegerField(default=0)
    quantity_cap = models.IntegerField(default=0)
    source = models.ForeignKey('SourceBuilding', null=True, on_delete=models.SET_NULL, related_name="buildings")

    def __str__(self):
        return "{0} (Game : {1}, Player : {2})".format(self.source.name,
                                                       self.player.game.pk,
                                                       self.player.pk)

    def __eq__(self, other):
        return (self.player.id == other.player.id and
                self.slug == other.slug and
                self.unlocked == other.unlocked and
                self.copies == other.copies)

    @property
    def player(self):
        return self.state.player

    @property
    def slug(self):
        return self.source.slug

    def is_purchasable(self):
        """
        Return the tuple (is_purchasable, error_message).
        error_message will be left empty if is_purchasable is true.
        """
        # Era check
        if self.player.game.era < self.source.era:
            return (False, "Ère trop précoce")
        # Parent technology check
        if not self.unlocked:
            return (False, "Technologie(s) nécessaire(s)")
        # Cost check
        if self.source.cost > self.player.resources.money:
            return (False, "Fonds insuffisants")
        if self.copies >= self.quantity_cap:
            return (False, "Nombre maximal de bâtiments constructibles atteints")
        return (True, "")

    def trigger_post_purchase_effects(self):
        """
        Update player statistics after self purchase.
        WARNING : the actual purchase should be done in a separate function.
        """

        # Spend money.
        self.player.resources.money -= self.source.cost
        self.player.resources.save()

        # Apply all modifiers.
        self.player.production.money += self.source.money_modifier
        self.player.production.food += self.source.food_modifier
        self.player.production.hydrocarbon += self.source.hydrocarbon_modifier
        self.player.production.electricity += self.source.electricity_modifier
        self.player.production.pollution += self.source.pollution_modifier
        self.player.production.waste += self.source.waste_modifier
        self.player.production.save()
        self.player.balance.economic += self.source.economic_modifier
        self.player.balance.social += self.source.social_modifier
        self.player.balance.environmental += self.source.environmental_modifier
        self.player.balance.save()

        # Execute self special effect.
        self.source.execute_special_effect()
