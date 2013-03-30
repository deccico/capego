from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db import transaction

import logging
logger = logging.getLogger(settings.APP_NAME)

def get_user(username):
    return User.objects.get(username = username)

class BadgeType(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=10)

class Badge(models.Model):
    def __unicode__(self):
        return self.name + " - " + self.type.name + " - " + self.description

    name = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(BadgeType)
    repetition_needed = models.IntegerField(default=1)
    description = models.TextField()

class UsersBadge(models.Model):
    def __unicode__(self):
        return self.user.username + "-" + self.badge.name

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    badge = models.ForeignKey(Badge)
    award_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("user", "badge"),)

class UserExtraData(models.Model):
    def __unicode__(self):
        return self.user.username

    user = models.OneToOneField(User)
    points = models.IntegerField(default=1)
    referrer = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='referrer')
    subscribes_to_newsletter = models.BooleanField(default=False)

    @staticmethod
    def getUserExtraData(user):
        if UserExtraData.objects.filter(user=user).count() > 0:
            return False,UserExtraData.objects.get(user=user)
        else:
            return True,UserExtraData(user=user)

    @staticmethod
    @transaction.commit_on_success
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

class UserActivity(models.Model):
    def __unicode__(self):
        return self.user.username + "-" + self.related_badge.name + "-" + self.description

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    related_badge = models.ForeignKey(Badge)
    description = models.CharField(blank=True, max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        #we use a triple composite key in order to let or avoid entering a duplicated activity when it is convenient
        #for example a badge for visiting three days in a row the site will need a different description while
        #we can avoid awarding a visit in the same day
        unique_together = (("user", "related_badge", "description"),)