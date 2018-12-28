from django.db import models
from .. import game_settings as constant

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # site_web = models.URLField(blank=True)
    # avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    # signature = models.TextField(blank=True)
    # inscrit_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return "Profil de {0}".format(self.user.username)
