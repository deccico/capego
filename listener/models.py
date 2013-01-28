from django.db import models
import json 

import formatter

class Language(models.Model):
    def __unicode__(self):
        return self.name 

    name = models.CharField(max_length=50)

#object that we can listen (nothing to do with the pattern)
class Listener(models.Model):
    def __unicode__(self):
        return "%s - %s" % (self.language, self.title)

    url = models.CharField(max_length=500)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1024, blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    language = models.ForeignKey(Language)
    length = models.SmallIntegerField(blank=True, null=True) #length in seconds
    dialog = models.TextField(max_length=8192, blank=True)
    
    aformatter = formatter.Formatter()
    
    @property
    def dialog_to_complete(self):
        return self.aformatter.dialog_to_complete(self.dialog)

    @staticmethod
    def get_good_line(listener_id, line_id):
        d = Listener.objects.get(id=listener_id).dialog
        return json.loads(d)[int(line_id)][1]

class Accent(models.Model):
    def __unicode__(self):
        return self.name 

    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language)


