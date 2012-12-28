from django.db import models
import json


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
    length = models.SmallIntegerField(blank=True, null=True) #lenght in seconds
    dialog = models.TextField(max_length=8192, blank=True)
    
    def get_formatted_dialog(self, dialog):
        """
        Format a dialog from this json format to nice html output
        [{0:'Hutz',1:'Bart'}, 
        [0,"All right, Gentlemen, I' retainer."], 
        [1,"No, money down! Oops, it."], ]        
        """
        dialog = json.loads(dialog)
        characters = dialog[0]
        html_output = """<table class="table table-striped table-condensed" id="dialog">
            <thead>
                <tr>
                    <th>Character </th>
                    <th>Text</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
            """
        for d in dialog[1:]:
            html_output += """
                            <tr><td><strong>%s:</strong></td>
                            <td>%s</td></tr>
                            """ % (characters[d[0]],d[1])
        html_output += """
                        </tbody>
                        <tfoot>
                            <tr>
                                <td colspan="6">
                                    <button class="btn btn-primary" onclick="refreshData()">
                                        Submit answers
                                    </button>
                                </td>
                            </tr>
                        </tfoot>
                        </table>        
                        """
        return html_output

class Accent(models.Model):
    def __unicode__(self):
        return self.name 

    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language)

#class Subtitle(models.Model):

