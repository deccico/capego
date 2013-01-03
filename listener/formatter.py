'''
Created on 01/01/2013

@author: adrian
'''

import json

import corrector

class Formatter():
    def __init__(self):
        self.corrector = corrector.Corrector()
        self.LINE_PREFIX = "line_id"
        self.SPAN_PREFIX = "span_id"
        self.SPAN_CORRECT_PREFIX = "span_correct_id"

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
            dialog_id_text = "%s%s" % (self.LINE_PREFIX, dialog_id)
            span_id_text = "%s%s" % (self.SPAN_PREFIX, dialog_id)
            span_correct_id_text = "%s%s" % (self.SPAN_CORRECT_PREFIX, dialog_id)
            html_output += """
                            <tr><td><strong>%s:</strong></td>
                            <td>%s</td></tr>
                            """ % (characters[d[0]],
                                   """
                                   <span id="%s">
                                   <span id="%s"></span>
                                   <input id="%s" type="text" 
                                   onkeyup="correct_data(event,%s,%s,%s)" 
                                   class="span11 search-query" 
                                   placeholder="Please enter %s dialog line here">
                                   </input></span>""" 
                                   % (span_id_text,
                                      span_correct_id_text, 
                                      dialog_id_text, 
                                      span_id_text, 
                                      dialog_id_text,
                                      span_correct_id_text,
                                      characters[d[0]]))
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
    
    def line_corrected(self, line, dialog_id):
        """
        from corrected dialog [[result, user_input_word]..[]]
        to html output
        """
        html_out = '<span id="%s%s">' % (self.SPAN_CORRECT_PREFIX, dialog_id)

        close_correct_span = True
        for i in range(len(line)):
            if line[i][0]:
                html_out += line[i][1] + " "
            else:
                html_out += "</span>"
                span_id_text = "%s%s" % (self.SPAN_PREFIX, dialog_id)
                dialog_id_text = "%s%s" % (self.LINE_PREFIX, dialog_id)
                corrected_id_text = "%s%s" % (self.SPAN_CORRECT_PREFIX, dialog_id)
                html_out += """
                            <input id="%s" type="text" onkeyup="correct_data(event,%s,%s,%s)" 
                            class="span11 search-query" 
                            value="%s">
                            </input>
                            """  % (dialog_id_text, 
                                    span_id_text, 
                                    dialog_id_text,
                                    corrected_id_text, 
                                    " ".join(w[1] for w in line[i:]))
                close_correct_span = False
                break
        if close_correct_span:
            html_out += "</span>"
        return html_out
    
