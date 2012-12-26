from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils import simplejson
from django.utils.functional import Promise
from django.utils.encoding import force_unicode
from models import Language, Listener, Accent

i =1
#here is some magic. We need to write custom JSON encoder, since sometimes
#serializing lazy strings can cause errors. 
#You need to write it only once and then can reuse in any app
class LazyEncoder(simplejson.JSONEncoder):
    """Encodes django's lazy i18n strings.
    """
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_unicode(obj)
        return obj

#here the view function starts
def check(request, listener_id):
    print "I'm here...."
    #===========================================================================
    # if request.is_ajax():
    #    print "I'm an Ajax request"
    #    #let built in simplejson package serialize our data. 
    #    #It means we transform everything to simple strings.
    #    result = simplejson.dumps({
    #        "message": "message-o",
    #        "type": "type-o",
    #    }, cls=LazyEncoder)
    #    return HttpResponse(result, mimetype='application/javascript')
    #===========================================================================
    return HttpResponse(getDialog())


def getDialog():
    dialog = """
        <table class="table table-striped table-condensed" id="dialog">
            <thead>
                <tr>
                    <th>Character </th>
                    <th>Text</th>
                    <th></th>
                </tr>
            </thead>
        
            <tbody>
                <tr>
                    <td><strong>Hutz:</strong></td>
                    <td>All right, Gentlemen, I'll take your case. But I'm going to have
                        to ask for a thousand dollar retainer.
                        </td>
                </tr>
                <tr>
                    <td><strong>Bart:</strong></td>
                    <td>A thousand dollars? But your ad says "No money down".
                    </td>
                </tr>
                <tr>
                    <td><strong>Hutz:</strong></td>
                    <td>
                    Oh! They got this all screwed up...
                    </td>
                </tr>
                <tr>
                    <td><strong>Bart:</strong></td>
                    <td>
                    So you don't work on a contingency basis?
                    </td>
                </tr>
                <tr class="status-correct">
                    <td><strong>Hutz:</strong></td>
                    <td class="status-correct">
                    No, money down! Oops, it shouldn't have this Bar Association 
                    logo here either.
                    </td>
                </tr>
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
    return dialog