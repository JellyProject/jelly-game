from django.db import models

from .. import game_settings as constant


class SourceBuilding(models.Model):
    """
        Source technology model.

        Fields :
            * name (char) : A unique human-readable name.
            * slug (char) : A simple and unique string to identify self.
            * version (char) : The game version self belongs to.
            * era (char) : The era self belongs to.
            * cost (int) : Money needed for purchase.
            * description (text) : A human-readable description.
            * parent_technology (OneToOne -> SourceTechnology) : A technology required before self may be purchased..
            * initial_quantity_cap (int) : The maximal number of buildings of this type purchasable at the beginning
            * money_modifier, hydrocarbon_modifier, food_modifier, electricity_modifier, pollution_modifier,
            * waste_modifier (int) : Production modifiers.
            * economic_modifier, social_modifier, environmental_modifier (int) : Balance modifiers.
            * hydrocarbon_consumption : hydrocarbon consumption of the building at each generation

    """
    special_effect_buildings = {
        "usine-avancee": "usine_avancee"
    }

    ''' Characteristics '''
    name = models.CharField(max_length=40, default='Old mansion', editable=False)
    slug = models.CharField(max_length=40, default='old-mansion', editable=False)
    version = models.CharField(max_length=20, default='jelly', editable=False)
    era = models.IntegerField(default=1, editable=False)
    description = models.TextField(default='A rather plain building.', editable=False)
    cost = models.IntegerField(default=1, editable=False)
    parent_technology = models.OneToOneField('SourceTechnology', on_delete=models.SET_NULL, null=True,
                                             related_name='child_building', editable=False)
    initial_quantity_cap = models.IntegerField(default=1, editable=False)

    ''' Production modifiers '''
    money_modifier = models.IntegerField(default=0, editable=False)
    hydrocarbon_modifier = models.IntegerField(default=0, editable=False)
    hydrocarbon_consumption = models.IntegerField(default=0, editable=False)
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

    def execute_special_effect(self):
        '''
            Call a callback function for buildings with a special effect
        '''
        method_prefix = self.special_effect_buildings.get(self.slug, "no_special_effect")
        if method_prefix != "no_special_effect":
            exec("self." + method_prefix + "_special_effect(self.version)")

    def usine_avancee_special_effect(self, version):
        if version == "jelly":
            print("Hello there")
