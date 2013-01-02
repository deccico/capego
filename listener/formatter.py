'''
Created on 01/01/2013

@author: adrian
'''

import json

class Formatter():
    def __init__(self):
        pass

    def dialog_corrected(self, dialog):
        """
        From the html dialog, return the formatted text 
            but with the class "status-correct" or "status-incorrect" 
            like in the following example 
            #                <tr class="status-correct">
            #                    <td><strong>Hutz:</strong></td>
            #                    <td class="status-correct">
            #                    No, money down! Oops, it shouldn't have this Bar Association 
            #                    logo here either.
            #                    </td>
            #                </tr>
        """
        fdialog = json.loads(dialog)
        characters = {}
        for i in range(len(fdialog[0])):
            characters[i] = fdialog[0][i]

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
        for d in fdialog[1:]:
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

    
    def dialog_to_complete(self, dialog):
        """
        Format a dialog from this json format to nice html output
        [{0:'Hutz',1:'Bart'}, 
        [0,"All right, Gentlemen, I' retainer."], 
        [1,"No, money down! Oops, it."], ]        
        """
        fdialog = json.loads(dialog)
        characters = {}
        for i in range(len(fdialog[0])):
            characters[i] = fdialog[0][i]

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
        dialog_id = 0
        for d in fdialog[1:]:
            dialog_id += 1
            dialog_id_text = "line_id%s" % (dialog_id)
            html_output += """
                            <tr><td><strong>%s:</strong></td>
                            <td>%s</td></tr>
                            """ % (characters[d[0]],
                                   """
                                   <input id="%s" type="text" onkeyup="correct_data(event,%s)" 
                                   class="span11 search-query" 
                                   placeholder="Please enter %s dialog line here"></input>""" 
                                   % (dialog_id_text, dialog_id_text, characters[d[0]]))
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
    