from django.conf import settings
from django.db import models

class Badge(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

class UsersBadge(models.Model):
    def __unicode__(self):
        return self.user.username + "-" + self.badge.name

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    badge = models.ForeignKey(Badge)

    class Meta:
        unique_together = (("user", "badge"),)
