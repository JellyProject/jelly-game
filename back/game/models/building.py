from django.db import models

from .. import game_settings as constant


class Building(models.Model):
    technology = models.OneToOneField('Technology', on_delete=models.SET_NULL, null=True)    # Technology required
    name = models.CharField(max_length=40, unique=True, default="Building")
    version = models.CharField(max_length=20, default='jelly')    # Version of the game
    description = models.TextField(default='A rather plain building.')

    ''' Production '''
    money = models.IntegerField(default=0)
    hydrocarbons = models.IntegerField(default=0)
    food = models.IntegerField(default=0)
    electricity = models.IntegerField(default=0)
    pollution = models.IntegerField(default=0)
    waste = models.IntegerField(default=0)

    def execute_special_effect(self):
        building_dict = {

        }
