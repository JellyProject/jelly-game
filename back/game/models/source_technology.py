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
    ''' Characteristics '''
    name = models.CharField(max_length=40, unique=True, default='Fire discovery')
    slug = models.CharField(max_length=40, unique=True, default='fire-discovery')
    version = models.CharField(max_length=20, default='jelly')
    era = models.IntegerField(default=1)
    description = models.TextField(default='Food may now be cooked.')
    cost = models.IntegerField(default=1)
    parent_technology = models.OneToOneField('SourceTechnology', on_delete=models.SET_NULL, null=True,
                                             related_name='child_technology')

    ''' Production modifiers '''
    money_modifier = models.IntegerField(default=0)
    hydrocarbon_modifier = models.IntegerField(default=0)
    food_modifier = models.IntegerField(default=0)
    electricity_modifier = models.IntegerField(default=0)
    pollution_modifier = models.IntegerField(default=0)
    waste_modifier = models.IntegerField(default=0)

    ''' Balance modifiers '''
    economic_modifier = models.IntegerField(default=0)
    social_modifier = models.IntegerField(default=0)
    environmental_modifier = models.IntegerField(default=0)
