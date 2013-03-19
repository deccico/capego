from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db import transaction

import logging
logger = logging.getLogger(settings.APP_NAME)

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

    user = models.OneToOneField(User)
    points = models.IntegerField(default=0)
    referrer = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='referrer')
    subscribes_to_newsletter = models.BooleanField(default=False)

    @staticmethod
    def getUserExtraData(user):
        if UserExtraData.objects.filter(user=user).count() > 0:
            return False,UserExtraData.objects.get(user=user)
        else:
            return True,UserExtraData(user=user)

    @staticmethod
    @transaction.commit_on_success #todo catch exception -> log -> reraise
    def save_additional_values(username, newsletter):
        try:
            user = get_user(username)
            is_new,user_extra_data = UserExtraData.getUserExtraData(user)
            if not is_new:
                return
            logger.info("saving: username:%s newsletter:%s" % (username, newsletter))
            user_extra_data.subscribes_to_newsletter = newsletter
            user_extra_data.save()
        except:
            logger.exception("failure while saving user additional data")
            raise

def get_user(username):
    return User.objects.get(username = username)