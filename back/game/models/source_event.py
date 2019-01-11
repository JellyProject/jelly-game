from django.db import models

from .. import game_settings as constant


class SourceEvent(models.Model):
    """
            Source event model.

            Fields :
                name (char) : A unique human-readable name.
                slug (char) : A simple and unique string to identify self.
                version (char) : The game version self belongs to.
                era (char) : The era self belongs to.
                description (text) : A human-readable description of self.
        """
    ''' Characteristics '''
    name = models.CharField(max_length=40, unique=True, default='Sunny day')
    slug = models.CharField(max_length=40, unique=True, default='sunny-day')
    version = models.CharField(max_length=20, default='jelly')
    era = models.IntegerField(default=1)
    description = models.TextField(default='There is nothing to report.')
