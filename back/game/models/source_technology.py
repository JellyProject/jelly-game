from django.db import models

from .. import game_settings as constant


class SourceTechnology(models.Model):
    """
        Source technology model.

        Fields :
            name (char) : A unique human-readable name.
            slug (char) : A simple and unique string to identify self.
            version (char) : The game version self belongs to.
            era (char) : The era self belongs to.
            description (text) : A human-readable description.
            cost (int) : Money needed for purchase.
            parent_technology (OneToOne -> SourceTechnology) : A technology required before self may be purchased.
            money_modifier, hydrocarbon_modifier, food_modifier, electricity_modifier, pollution_modifier,
            waste_modifier (int) : Production modifiers.
            economic_modifier, social_modifier, environmental_modifier (int) : Balance modifiers.
    """
    special_effect_technologies = {
    }

    ''' Characteristics '''
    name = models.CharField(max_length=40, default='Fire discovery', editable=False)
    slug = models.CharField(max_length=40, default='fire-discovery', editable=False)
    version = models.CharField(max_length=20, default='jelly', editable=False)
    era = models.IntegerField(default=1, editable=False)
    description = models.TextField(default='Food may now be cooked.', editable=False)
    cost = models.IntegerField(default=1, editable=False)
    parent_technology = models.OneToOneField('SourceTechnology', on_delete=models.SET_NULL, null=True,
                                             related_name='child_technology', editable=False)

    ''' Production modifiers '''
    money_modifier = models.IntegerField(default=0, editable=False)
    hydrocarbon_modifier = models.IntegerField(default=0, editable=False)
    food_modifier = models.IntegerField(default=0, editable=False)
    electricity_modifier = models.IntegerField(default=0, editable=False)
    pollution_modifier = models.IntegerField(default=0, editable=False)
    waste_modifier = models.IntegerField(default=0, editable=False)

    ''' Balance modifiers '''
    economic_modifier = models.IntegerField(default=0, editable=False)
    social_modifier = models.IntegerField(default=0, editable=False)
    environmental_modifier = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return "{0} (Version : {1})".format(self.name, self.version)

    class Meta:
        verbose_name = "Source technology"
        verbose_name_plural = "Source technologies"

    def execute_special_effect(self):
        '''
            Call a callback function for technologies with a special effect
        '''
        method_prefix = self.special_effect_technologies.get(self.slug, "no_special_effect")
        if method_prefix != "no_special_effect":
            exec("self." + method_prefix + "_special_effect(self.version)")
