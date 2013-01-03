'''
Created on 01/01/2013

@author: adrian
'''

import re

class Corrector():
    def __init__(self):
        self.RE_REMOVE_CHARS = "\W"
        self.WORD_SEP = [" ", ".",",","'"]
        self.re_remove = re.compile(self.RE_REMOVE_CHARS)
        self.EQUIV = {"ll": "will", "m":"am"}
    
    def correct_dialog(self, good_one, user_input):
        """
        from the user dialog and correct dialog
        returns a list of [[result, user_input_word]..[]]
        """
        good_one = self.strip_signs(good_one)
        user_input = self.strip_signs(user_input)
        out = []
        for i in range(len(user_input)):
            wu = self.get_word(user_input[i]) #worduser
            gw = self.get_word(good_one[i])     #goodword
            result = (wu==gw)
            out.append([result,wu])        
        #add an incomplete mark to the user input
        if len(user_input) < len(good_one):
            out.append([False,""]) 
        return out 
    
    def strip_signs(self, line):
        lines = self.re_remove.split(line)
        lines = [l.lower() for l in lines if len(l)>0] 
        return lines

    def list_to_string(self, list_line):
        out = ""
        for l in list_line:
            out += l + " "
        return out
    
    #todo: use memoize pattern
    def get_word(self,word):
        return word if word not in self.EQUIV.keys() else self.EQUIV[word]
    
    def format_line(self, line):
        #todo this function
        return self.list_to_string([w[1] for w in line])
        
        
        