from django.db import models


class Language(models.Model):
    def __unicode__(self):
       return self.name 

    name = models.CharField(max_length=50)

#object that we can listen (nothing to do with the pattern)
class Listener(models.Model):
    def __unicode__(self):
       return "%s-%s-%s" % (self.language, self.title, self.url)

    url = models.URLField()
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1024, blank=True)
    pub_date = models.DateTimeField('date published',auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    broken = models.BooleanField()
    language = models.ForeignKey(Language)
    length = models.SmallIntegerField(blank=True, null=True) #lenght in seconds

class Accent(models.Model):
    def __unicode__(self):
       return self.name 

    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language)

