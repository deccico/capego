import logging
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db import transaction

logger = logging.getLogger(settings.APP_NAME)


def get_user(username):
    return User.objects.get(username = username)

class Activity(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=20)

class BadgeType(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=10)

class Badge(models.Model):
    def __unicode__(self):
        return self.name + " - " + self.type.name + " - " + self.description

    name = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(BadgeType)
    related_activity = models.ForeignKey(Activity)
    repetition_needed = models.IntegerField(default=1)
    description = models.TextField()

class UserBadge(models.Model):
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
            UserActivity(user=user, related_activity=Activity.objects.get(name="Sign up")).save()
        except:
            logger.exception("failure while saving user additional data")
            raise

class UserActivity(models.Model):
    def __unicode__(self):
        return self.user.username + "-" + self.related_activity.name + "-" + self.description

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    related_activity = models.ForeignKey(Activity)
    description = models.CharField(blank=True, max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    @transaction.commit_on_success
    def save(self, *args, **kwargs):
        super(UserActivity, self).save(*args, **kwargs)
        Awarder().analyze_activity(self)

    class Meta:
        #we use a triple composite key in order to let or avoid entering a duplicated activity when it is convenient
        #for example a badge for visiting three days in a row the site will need a different description while
        #we can avoid awarding a visit in the same day
        unique_together = (("user", "related_activity", "description"),)




class Awarder():
    def analyze_activity(self, user_activity):
        #get related badges
        number_of_activities = UserActivity.objects.filter(user=user_activity.user, related_activity=user_activity.related_activity).count()
        badges_to_award = Badge.objects.filter(related_activity=user_activity.related_activity)
        badges_awarded = UserBadge.objects.filter(user=user_activity.user)

        for b in badges_to_award:
            #check if repetitions are enough for a new badge
            if b in badges_awarded:
                continue
            if b.repetition_needed <= number_of_activities:
                self.award_badge(user_activity.user, b)


    def award_badge(self, user, badge):
        UserBadge(user=user, badge=badge).save()