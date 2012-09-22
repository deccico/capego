from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50)

#object that we can listen (nothing to do with the pattern)
class Listener(models.Model):
    src = models.CharField(max_length=1024)
    pub_date = models.DateTimeField('date published')
    update_date = models.DateTimeField()
    broken = models.BooleanField()
    language = models.ForeignKey(Language)

class Accents(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language)

