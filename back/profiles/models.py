from django.db import models
from core.models import TimestampedModel


class Profile(TimestampedModel):
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )
    motto = models.TextField(blank=True)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
