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
    name = models.CharField(max_length=40, unique=True, default='Sunny day', editable=False)
    slug = models.CharField(max_length=40, unique=True, default='sunny-day', editable=False)
    version = models.CharField(max_length=20, default='jelly', editable=False)
    era = models.IntegerField(default=1, editable=False)
    description = models.TextField(default='There is nothing to report.', editable=False)

    def __str__(self):
        return "{0} (Version : {1})".format(self.name, self.version)
