from django.db import models

from .. import game_settings as constant


class Event(models.Model):
    """
    Event model

    Fields :
        * game (ForeignKey -> Game) : game in which this event will occure
        * source (OneToOne -> SourceEvent) : source event corresponding
        * index (int) : index of this event in the 'event deck'
    """
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name="events", editable=False)
    source = models.OneToOneField('SourceEvent', null=True, on_delete=models.SET_NULL)

    index = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return "{0} (Game : {1})".format(self.source.name, self.game.pk)

    def execute_effect(self):
        self.source.execute_effect(self.game)
