from django.db import models

class NewsletterSubscriber(models.Model):
    def __unicode__(self):
        return self.email

    email = models.CharField(max_length=100, unique=True)

class UsersContactingCapego(models.Model):
    def __unicode__(self):
        return self.name + "-" + self.email

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    message = models.CharField(max_length=1024)

