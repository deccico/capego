from django.conf import settings
from django.db import models

class BadgeType(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=10)

class Badge(models.Model):
    def __unicode__(self):
        return self.name + " - " + self.type.name + " - " + self.description

    name = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(BadgeType)
    description = models.TextField()

class UsersBadge(models.Model):
    def __unicode__(self):
        return self.user.username + "-" + self.badge.name

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    badge = models.ForeignKey(Badge)

    class Meta:
        unique_together = (("user", "badge"),)

class UserExtraData(models.Model):
    def __unicode__(self):
        return self.user.username

    user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True)
    points = models.IntegerField()
    referrer = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='referrer_user')
    subscribes_to_newsletter = models.BooleanField()
