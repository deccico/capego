from django.conf import settings
from django.db import models

class Badge(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

class UsersBadges(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    badge_type = models.ForeignKey(Badge)

