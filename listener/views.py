from django.http import HttpResponse
from models import Listener


#here the view function starts
def check(request, listener_id):
    return HttpResponse(getDialog(listener_id))


def getDialog(listener_id):
    l = Listener.objects.get(id=listener_id)
    #return l.dialog
    return l.get_formatted_dialog(l.dialog)
 
# 
# dialog = """
#        <table class="table table-striped table-condensed" id="dialog">
#            <thead>
#                <tr>
#                    <th>Character </th>
#                    <th>Text</th>
#                    <th></th>
#                </tr>
#            </thead>
#        
#            <tbody>
#                <tr>
#                    <td><strong>Hutz:</strong></td>
#                    <td>All right, Gentlemen, I'll take your case. But I'm going to have
#                        to ask for a thousand dollar retainer.
#                        </td>
#                </tr>
#                <tr>
#                    <td><strong>Bart:</strong></td>
#                    <td>A thousand dollars? But your ad says "No money down".
#                    </td>
#                </tr>
#                <tr>
#                    <td><strong>Hutz:</strong></td>
#                    <td>
#                    Oh! They got this all screwed up...
#                    </td>
#                </tr>
#                <tr>
#                    <td><strong>Bart:</strong></td>
#                    <td>
#                    So you don't work on a contingency basis?
#                    </td>
#                </tr>
#                <tr class="status-correct">
#                    <td><strong>Hutz:</strong></td>
#                    <td class="status-correct">
#                    No, money down! Oops, it shouldn't have this Bar Association 
#                    logo here either.
#                    </td>
#                </tr>
#            </tbody>
#            <tfoot>
#                <tr>
#                    <td colspan="6">
#                        <button class="btn btn-primary" onclick="refreshData()">
#                            Submit answers
#                        </button>
#                    </td>
#                </tr>
#            </tfoot>
#        </table>
#    """
#===============================================================================