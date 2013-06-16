import json

import corrector

class Formatter():
    def __init__(self):
        self.corrector = corrector.Corrector()
        self.LINE_PREFIX = "line_id"
        self.SPAN_PREFIX = "span_id"
        self.SPAN_CORRECT_PREFIX = "span_correct_id"
        self.BTN_SUGGEST_PREFIX = "btn_suggest"

    def dialog_to_complete(self, dialog, listener_id):
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
                    <th class="minimum_width">Character</th>
                    <th class="minimum_width"></th>
                    <th>Text</th>
                </tr>
            </thead>
            <tbody>
            """
        dialog_id = 0
        for d in fdialog[1:]:
            dialog_id += 1
            btn_suggest = "%s%s" % (self.BTN_SUGGEST_PREFIX, dialog_id)
            dialog_id_text = "%s%s" % (self.LINE_PREFIX, dialog_id)
            span_id_text = "%s%s" % (self.SPAN_PREFIX, dialog_id)
            span_correct_id_text = "%s%s" % (self.SPAN_CORRECT_PREFIX, dialog_id)
            btn_next_word = 'onclick="send_correction(getXmlHttp(),%s,%s,%s,true,%s,%s)">' % (span_id_text, dialog_id_text, span_correct_id_text, listener_id, btn_suggest)
            character = characters[d[0]]
            html_output += """
                            <tr><td><strong>%s:</strong></td><td>
                            <button id="%s" tabIndex="-1" class="small-btn" 
                            title="Help me with the next word" %s
                            <i class="icon-eye-open"></i></button>
                            </td>
                            <td>%s</td></tr>
                            """ % (character,
                                   btn_suggest,
                                   btn_next_word,
                                   """
                                   <span id="%s">
                                   <span id="%s"></span>
                                   <textarea id="%s"
                                   onkeyup="correct_data(event,%s,%s,%s,%s,%s)"
                                   class="span11 search-query"
                                   placeholder="Please enter %s dialog line here"></textarea></button></span>"""
                                   % (span_id_text,
                                      span_correct_id_text, 
                                      dialog_id_text, 
                                      span_id_text, 
                                      dialog_id_text,
                                      span_correct_id_text,
                                      listener_id,
                                      btn_suggest,
                                      character))
        html_output += """
                        </tbody>
                        <tfoot>
                            <tr>
                                <td colspan="6" >
                                    <button id="btn_correct" class="m-btn blue btn-block" onclick="correct_everything(%s,%s)">
                                        Submit answers
                                    </button>
                                </td>
                            </tr>
                        </tfoot>
                        </table>        
                        """ % (len(fdialog[1:]), listener_id)
        return html_output
    
    def line_corrected(self, is_correct, line, dialog_id, listener_id):
        """
        from corrected dialog [[result, user_input_word]..[]]
        to html output
        """
        html_out = '<div class="%s">' % ("status-correct" if is_correct else "")
        html_out += '<span><i class="%s"></i> </span>' % ("icon-ok" if is_correct else "") 
        html_out += '<span id="%s%s">' % (self.SPAN_CORRECT_PREFIX, dialog_id)

        close_correct_span = True
        for i in range(len(line)):
            if line[i][0]:
                html_out += line[i][1] + " "
            else:
                html_out += "</span>"
                btn_suggest = "%s%s" % (self.BTN_SUGGEST_PREFIX, dialog_id)
                span_id_text = "%s%s" % (self.SPAN_PREFIX, dialog_id)
                dialog_id_text = "%s%s" % (self.LINE_PREFIX, dialog_id)
                corrected_id_text = "%s%s" % (self.SPAN_CORRECT_PREFIX, dialog_id)
                input_text = " ".join(w[1] for w in line[i:]).strip()
                html_out += """
                            <textarea id="%s" onkeyup="correct_data(event,%s,%s,%s,%s,%s)"
                            class="span11 search-query"
                            placeholder = "Please enter the rest of the dialog here.">%s</textarea>
                            """  % (dialog_id_text, 
                                    span_id_text, 
                                    dialog_id_text,
                                    corrected_id_text,
                                    listener_id,
                                    btn_suggest,
                                    input_text
                                    )
                close_correct_span = False
                break
        if close_correct_span:
            html_out += "</span>"
        html_out += "</div>"
        return html_out
