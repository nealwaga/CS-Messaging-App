from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

# Create here
class Agent(AbstractUser):
    full_name = models.CharField(_('Full Name'), max_length=100, blank=False, null=False)
    email = models.EmailField(_('Email Address'), unique=True, null=False, db_index=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.email)