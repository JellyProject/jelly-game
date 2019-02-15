import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from core.models import TimestampedModel


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """ Create and return a `User` with an email, username and password. """
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email address.')
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        """ Create and return a `User` with superuser (admin) permissions. """
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']    # username and password will be prompted by default
    objects = UserManager()

    @property
    def token(self):
        """ Define an alias for `user._generate_jwt_token()`. """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Generate a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        expiry_date = datetime.now() + timedelta(days=60)
        token = jwt.encode({'id': self.pk, 'expire': int(expiry_date.strftime('%s'))},
                           settings.SECRET_KEY,
                           algorithm='HS256')
        return token.decode('utf-8')
